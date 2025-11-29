import paho.mqtt.client as mqtt
import threading
import os
import time
import json

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

BROKER = "localhost"
PORT = 1883

# Topics for each sensor
SENSORS = {
    "Temperature": "areen/temp",
    "Humidity": "areen/humidity",
    "People Counter": "areen/people"
}

# Subscriber function

def create_subscriber(sensor_name, topic):
    """Subscribe to a topic and log messages in JSON format."""
    log_file = f"logs/{sensor_name.lower().replace(' ', '_')}_sub.log"

    def on_message(client, userdata, msg):
        """Callback function when a message is received."""
        payload = msg.payload.decode()
        received_at = time.ctime()

        try:
            data = json.loads(payload)  # Parse JSON
        except json.JSONDecodeError:
            data = {"value": payload, "unit": "unknown", "student_id": "unknown"}

        entry = {
            "sensor": sensor_name,
            "topic": msg.topic,
            "payload": data,
            "received_at": received_at
        }

        # Write log
        with open(log_file, "a") as f:
            f.write(f"{entry['received_at']} {entry['payload']}\n")

        # Print nicely
        print(f"{sensor_name} Received: {data['value']} {data['unit']} (Student ID: {data['student_id']})")
        print(f"Logged entry: {entry['received_at']} {entry['payload']}")

    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.subscribe(topic)
    client.on_message = on_message
    print(f"{sensor_name} Subscriber is listening...")
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print(f"{sensor_name} Subscriber stopped.")
        client.disconnect()

# Main function

def main():
    """Run all subscribers in separate threads."""
    threads = []
    for sensor, topic in SENSORS.items():
        thread = threading.Thread(target=create_subscriber, args=(sensor, topic))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
