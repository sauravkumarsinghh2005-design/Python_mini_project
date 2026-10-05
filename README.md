# Smart Room Temperature Control System (CPS)

## Aim
Design a Python-based Cyber-Physical System that monitors room temperature and automatically controls a cooling fan.

## CPS components

| CPS part | Implementation |
| --- | --- |
| Physical environment | `Room` model with heat gain and cooling |
| Sensor | `TemperatureSensor` produces a reading with small measurement noise |
| Controller | `CoolingController` applies threshold-based logic |
| Actuator | Fan is switched ON/OFF |
| Feedback loop | Every reading updates the next control decision |

## Control rule

* Turn the fan **ON** when temperature is at least **30°C**.
* Turn the fan **OFF** when temperature is at most **27°C**.
* Between 27°C and 30°C, retain its current state. This is *hysteresis*, which avoids rapid switching.

## How to run

1. Install Python 3.10 or later.
2. In this project folder, run `pip install -r requirements.txt`.
3. Run `python smart_room_cps.py`.

The program prints live sensor data and creates `temperature_log.csv` plus `temperature_graph.png`.

## Hardware extension (optional)

For a real prototype, replace the simulated sensor with a DHT11/DHT22 sensor connected to a Raspberry Pi or ESP32, and replace `fan_on` with a relay-control command.
