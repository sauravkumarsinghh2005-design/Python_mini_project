# Mini Project Report: Smart Room Temperature Control System

## Abstract

This project implements a Cyber-Physical System (CPS) for smart-room temperature regulation. A temperature sensor continuously observes the room, a controller decides whether cooling is required, and a fan acts on the physical environment. Python is used to simulate the sensor, room behavior and actuator. The result demonstrates the feedback-loop principle central to CPS.

## Objectives

1. Monitor the temperature of a room.
2. Automatically activate cooling when the room becomes too warm.
3. Avoid frequent fan switching using hysteresis.
4. Record temperature and actuator status for analysis.

## System design

`Room → Temperature Sensor → Controller → Fan → Room`

The room is the physical process. The sensor measures its temperature, the controller compares it against limits, and the fan reduces the room temperature. The changed temperature is measured again, forming a closed feedback loop.

## Methodology

The simulation begins with a warm room. In each cycle, the sensor returns a measured temperature, including small noise to make the system realistic. If the reading reaches 30°C, the controller turns the fan on. The fan remains on until the temperature falls to 27°C or lower. The program stores every reading in a CSV file and plots the result.

## Software requirements

* Python 3.10+
* matplotlib (for graph generation)

## Results and discussion

The generated graph shows temperature increasing toward the external temperature while the fan is off. At the upper threshold, the controller enables cooling and temperature falls. Hysteresis keeps the fan state stable between the two thresholds. This demonstrates autonomous sensing, computation, control and physical response.

## Conclusion

The Smart Room Temperature Control System successfully models a basic CPS feedback loop. It can be extended into an IoT project by using real sensors, a microcontroller, a relay module and a mobile dashboard.

## Future scope

* Send alerts to a phone through MQTT or Telegram.
* Use machine learning to predict temperature changes.
* Control multiple rooms from one dashboard.
* Add humidity and occupancy sensors.
