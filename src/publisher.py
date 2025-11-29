import paho.mqtt.client as mqtt
import time
import json
import random
import os
import threading

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

BROKER = "localhost"
PORT = 1883
STUDENT_ID = "12217557"

# Functions to generate sensor values

def temperature_value():
    """ random temperature between 18 and 30 """
    return round(random.uniform(18.0, 30.0), 2)

def humidity_value():
    """ random humidity value between 25% and 90%."""
    return round(random.uniform(25.0, 90.0), 2)

def people_counter_value():
    """ random people count between 0 and 50."""
    return random.randint(0, 50)

# Publisher functions

def publish_temperature(client):
    """Publish random temperature readings every 2 seconds."""
    topic = "areen/temp"
    unit = "C"
    while True:
        value = temperature_value()
        message = {"value": value, "unit": unit, "student_id": STUDENT_ID}
        client.publish(topic, json.dumps(message))
        print(f"Temperature Published: {message}")
        with open("logs/temp_pub.log", "a") as f:
            f.write(f"{time.ctime()} {message}\n")
        time.sleep(2)

def publish_humidity(client):
    """Publish random humidity readings every 2 seconds."""
    topic = "areen/humidity"
    unit = "%"
    while True:
        value = humidity_value()
        message = {"value": value, "unit": unit, "student_id": STUDENT_ID}
        client.publish(topic, json.dumps(message))
        print(f"Humidity Published: {message}")
        with open("logs/humidity_pub.log", "a") as f:
            f.write(f"{time.ctime()} {message}\n")
        time.sleep(2)

def publish_people_counter(client):
    """Publish random people count every 2 seconds."""
    topic = "areen/people"
    unit = "count"
    while True:
        value = people_counter_value()
        message = {"value": value, "unit": unit, "student_id": STUDENT_ID}
        client.publish(topic, json.dumps(message))
        print(f"People Counter Published: {message}")
        with open("logs/people_pub.log", "a") as f:
            f.write(f"{time.ctime()} {message}\n")
        time.sleep(2)

# Main function

def main():
    """Main function to run all publishers."""
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    print("Publisher started for all sensors...")

    # Run each publisher in a separate thread
    threading.Thread(target=publish_temperature, args=(client,)).start()
    threading.Thread(target=publish_humidity, args=(client,)).start()
    threading.Thread(target=publish_people_counter, args=(client,)).start()

if __name__ == "__main__":
    main()
