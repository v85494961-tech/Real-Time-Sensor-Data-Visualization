# Real-Time Light Detection System
A beginner embedded systems project demonstrating real-time light detection and visualization using an Arduino Uno, an LDR sensor module and python.
The system monitors ambient light conditions using the LDR module. Arduino processes the sensor input and transmits the data through serial communication, while python visualizes the incoming data in real time using matplotlib.

## Features
- Real-time light detection
- Serial communication between Arduino and python
- live data visualization using matplotlib
- Hardware-software integration
- Beginner embedded systems flow

## Hardware Used
- Arduino Uno
- LDR Sensor Module
- USB cable
- Laptop

## Software & Libraries
### Software 
- Arduino IDE
- python 3

### Python Libraries
- Pyserial
- Matplotlib

## System Workflow
- The LDR sensor detects changes in ambient light
- Arduino reads the sensor state using digital input
- Sensor data is transmitted through serial communication
- Python receives the incoming data
- Matplotlib plots the data in real time

## Project Files
- 'Arduino_code.ino' - Arduino program for sensor monitoring
- 'Serial_plotter.py' - Python script for real-time plotting

## Circuit Diagram
![Circuit Diagram](arduino_ldr.png)

## Screenshots
### Live Plot Output
![Graph Output](graph_output.png)

### Hardware Setup
![Hardware Setup](hardware_setup.png)

### Arduino code
![Arduino Code](arduino_code.png)

## Learning Outcomes
Through this project, i learned:
- Serial communication between Arduino and python
- Real-time data visualization
- sensor interfacing with Arduino
- embedded systems fundamentals
- Hardware-software integration workflows

## Challenges Faced
- Initially selected the wrong COM port when connecting Arduino to Python.
- Sensor readings fluctuated even under constant lighting conditions.
- Experienced delays in live plotting due to high data transmission rates.
- Ensured the baud rate configuration matched in both Arduino and Python.
- Learned that the Arduino, Serial Monitor and Python script cannot access the same serial port simultaneously

## Impact / Applications
- Helps in understanding real-time light sensing using embedded systems.
- Shows how physical sensor data can be converted into useful digital information.
- Demonstrates basic principles used in IoT monitoring systems.
- Can be expanded into smart lighting or automatic lighting control systems.
- Builds foundation for real-time data acquisition and visualization systems.
- Useful for learning how hardware and software systems work together.

## Future Improvements
- Add analog light intensity monitoring
- Store sensor data for analysis
- Integrate ESP32 for IoT connectivity
- Add automatic lighting control functionality

## Technologies
- Embedded Systems
- Arduino
- Python
- Matplotlib
- Serial Communication
- IoT Foundations

## Author
- Vincent Panyako
- Electrical and Communication Engineering student

  




