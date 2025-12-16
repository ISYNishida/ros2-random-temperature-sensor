# ROS2 Virtual Temperature Sensor Example

This repository contains a simple ROS2 (Humble) example to demonstrate  
publisher/subscriber communication using virtual temperature sensors.

## Overview

- Sensor A: publishes random temperature (0–40°C)
- Sensor B: publishes random temperature (-10–10°C)
- Subscriber: receives temperature data from both sensors
- Demonstrates ROS2 pub/sub and loose coupling

## Environment

- ROS2 Humble
- Tested on Docker + WSL2 (Ubuntu 22.04)

## Build

```bash
cd ros2_ws
colcon build
source install/setup.bash
```

## Run

### Sensor A

```bash
ros2 run random_temperature_sensor temperature_publisher
```

### Sensor B

```bash
ros2 run random_temperature_sensor temperature_publisher_b
```

### Subscriber

```bash
ros2 run random_temperature_sensor temperature_subscriber
```

## Notes

This code is provided as-is for educational purposes.
