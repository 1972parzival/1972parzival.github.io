---
categories: ["Electronics & Arduino"]
date: '2025-10-06'
description: "Include Statements: The code includes necessary libraries for communication with the GPS module, parsing GPS data, and controlling the OLED display. Serial and Variable Initialization: SoftwareSerial setup."
image: "/assets/images/img-8282-5184x3456.jpg"
slug: archie-page-7
tags: []
title: GPS device
---


### GPS System Using Arduino and OLED Display: Part 1




![Mobirise Website Builder](/assets/images/img-8283-1836x1224.jpg)




### Frequently asked questions


- An Electronic circuit is composed of individual electronic components, such as resistors, transistors, capacitors, inductors and diodes, connected by conductive wires or traces through which electric current can flow.


- GPS module The BN-880 is a GPS module designed for precise and reliable global positioning and navigation applications. It combines GPS (Global Positioning System) and GLONASS (Global Navigation Satellite System) capabilities, utilizing multiple satellite constellations for enhanced accuracy and performance. Equipped with an integrated magnetometer (compass), the BN-880 also offerss orientation information (not used in this project). Its compact design and compatibility with various platforms make it suitable for a wide range of applications, including drones, robotics, and other navigation-dependent systems, where accurate positioning and heading information are crucial.


- Arduino Uno?  An Arduino Uno is a microcontroller board designed for beginners and hobbyists: It is an open-source platform, making it easy to use and modify for various projects. An Arduino Uno has input and output pins that allow you to connect sensors, actuators, and other components. With its user-friendly integrated development environment (IDE), you can write and upload code to control electronic devices, making it an excellent choice for prototyping and learning electronics.


- 128x64 OLED LCD display? This is a small screen that can show information in a clear and easy-to-read way. The "128x64" part means it has 128 pixels in width and 64 pixels in height, which together make up the picture on the screen. "OLED" stands for Organic Light-Emitting Diode, a technology that allows each pixel to emit its own light, resulting in vibrant colors and deep blacks. This type of display is often used in devices like watches, fitness trackers, and other gadgets where space is limited but a sharp and bright screen is important.




![Mobirise Website Builder](/assets/images/1-517x689.jpg)


![Mobirise Website Builder](/assets/images/2-1-441x723.jpg)


![Mobirise Website Builder](/assets/images/3-1-533x500.jpg)


![Mobirise Website Builder](/assets/images/4-350x534.jpg)


![Mobirise Website Builder](/assets/images/5-550x623.jpg)




#### Code Breakdown


Include Statements:

The code includes necessary libraries for communication with the GPS module, parsing GPS data, and controlling the OLED display.


Serial and Variable Initialization:


SoftwareSerial GPSSerial(3, 4);: Initializes a software serial communication instance for GPS, using pins 3 (RX) and 4 (TX).

TinyGPSPlus GPS;: Creates an instance of the TinyGPSPlus library to parse GPS data.

GyverOLED oled;: Initializes the OLED display instance using the GyverOLED library.

Int x = 1; int y = 5;: Initializes integer variables x and y with values.


Setup Function: Initializes the serial communication for debugging.

Initializes the GPS serial communication.

Initializes the OLED display.

Clears the OLED display.

Updates the OLED display.

Loop Function: Contains two main blocks of code, one dependent on the value of x and the other for processing GPS data.

Conditional Block for x == 1: Generates and displays random dots on the OLED display.

Updates the display with each dot.

Introduces delays between updates.

Clears the OLED display after the loop.

While Loop for GPS Data: Continuously checks if there is data available from the GPS module.

Reads and processes GPS data using GPS. Encode() method.

If GPS location data is updated, enters the conditional block within this loop.

GPS Data Handling Block: Handles various interactions with the OLED display based on GPS location updates.

Displays animations and messages on the OLED.

Prints latitude and longitude data to both the OLED and the serial monitor.

Conditional Display Changes based on x and y: Displays animations and messages on the OLED based on values of x and y.

Manipulates the y variable to create dynamic animations. TLDR: The code essentially handles communication with the GPS module, parsing its data, and displaying relevant information on the OLED display. It incorporates animations and messages to indicate GPS signal detection and location updates.




#### Video Demo


![Mobirise Website Builder](/assets/images/img-8248-5184x3456.jpg)




Final GPS system GIF.


![Mobirise Website Builder](/assets/images/GPS-rotate.gif)


