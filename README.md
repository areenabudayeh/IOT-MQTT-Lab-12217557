# MQTT Mosquitto-Paho Project

A simple IoT project using **Mosquitto MQTT Broker** and **Paho MQTT
Client** in Python to simulate sensor data (temperature, humidity,
people counter) and subscribe to their topics.

------------------------------------------------------------------------

## Overview

This project includes: - Multiple MQTT **publishers** sending random
sensor values every few seconds. - Multiple MQTT **subscribers**
listening to each topic separately. - All messages include the **student
ID: 12217557**. - Every message received or sent is saved into log
files.

------------------------------------------------------------------------

## Requirements

-   Python 3\
-   Mosquitto MQTT Broker\
-   Paho-MQTT library

------------------------------------------------------------------------

## Installation

Install the required Python library:

``` bash
pip install paho-mqtt
```

Start the Mosquitto broker:

``` bash
mosquitto
```

------------------------------------------------------------------------

## Usage

### Run Publishers

This will publish temperature, humidity, and people counter values
automatically:

``` bash
python publisher.py
```

### Run Subscribers

This will listen to the topics and log all incoming messages:

``` bash
python subscriber.py
```

------------------------------------------------------------------------

## Description

-   The publisher sends data to:
    -   areen/temp
    -   areen/humidity
    -   areen/people
-   Subscribers listen to the topics and print/log the data instantly.

Each message is a JSON payload that contains: - sensor value\
- unit\
- timestamp\
- **student ID: 12217557**


