---
categories: ["Software & Programming"]
date: '2025-10-06'
description: "many of the areas of text, images or information is not final"
image: "/assets/images/img-8239-5184x3456.JPG"
slug: archie-page-9
tags: []
title: IR device
---


### IR Device project




![Mobirise Website Builder](/assets/images/wide-1836x1224.JPG)




##### This is a work in progress project


Many of the areas of text, images or information is not final




### IR?


Graph showing the Electromagnetic wavelength of IR


IR (Infrared): IR stands for Infrared, which is a type of electromagnetic radiation that is not visible to the human eye. It has longer wavelengths than visible light and is often used for wireless communication, remote controls, and heat detection, among other applications.


IR Signals: IR signals refer to the communication or transmission of data using infrared light. In devices like remote controls or IR sensors, information is encoded and transmitted as bursts of IR light, which are then received and decoded by the corresponding receiver to perform a specific action, such as controlling a TV or transferring data between devices.


![Mobirise Website Builder](/assets/images/infrared-spectrum-644x426.JPG)




If direction connections between devices (like a cable) are like a  metal pipes of flowing water, then IR signals are like waves of information in a ocean. A lot less direct and a lot more natural interference.




### Code Breakdown


(CLIck on image for GitHub code)


The Program was made to control an IR (Infrared) remote control receiver and display information on an OLED screen. The code defines and initializes various variables, including arrays for storing IR codes, sets of default IR codes, and a custom IR code array. It also managess a program mode for manually inputting and storing IR codes. The program mode is triggered by a button press, and during this mode, the code listens for IR signals, stores them in an array, and checks for duplicate entries. Once ten unique IR codes are collected, the program mode is exited. In the main loop, it continuously listens for IR signals and performs actions based on the received IR codes. It displays the received IR code and a counter on the OLED screen, and it can detect and handle repeat commands.


The code also features a boot-up animation on the OLED screen when the device starts, which includes drawing lines and displaying "BLACK OUT IR DEVICE WAITING FOR IR SIGNAL." text. The button on pin 4 triggers the program mode, and the code performs different actions based on the received IR codes. If a received IR code matches one of the predefined default codes, it prints a corresponding message, and if the code detects a repeat command, it uses the last command stored. Overall, this code is designed to receive and respond to IR remote control commands, with a program mode to manually input and store custom IR codes.


![Mobirise Website Builder](/assets/images/ir-code-940x958.JPG)




### Hardware design


(Breakdown of basic elements of IR device)


We are using a 0.96 inch I2C OLED display to display:- what the command value (#) is- the number of commands sent- if this command is new or sent as a repeat codewe are using the IR receiver to receive the raw IR values from the remote we are using the buttons to help make a custom raw value array and allow for soft reprograming (WIP) Arduino mega is used for processing and control


![Mobirise Website Builder](/assets/images/untitled-1076x895.JPG)




#### VIDEO DEMO


