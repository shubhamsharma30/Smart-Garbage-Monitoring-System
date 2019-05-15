					﻿Water Level Detector Project

Step 1: Components Required :
	
You will need the following materials for making your own Water Level Detector

>Arduino Uno

>Ultrasonic Sensor (HC-SR04)

>Jumper wires

>4 Digit seven segment display

Step 2:  Connect Arduino Uno With HC-SR04 and 4 Digit Seven Segment Display : 

	HC-SR04                 Arduino Uno
         
	 GND	                 GND
         
         ECHO                    D9

         TRIG                    D8

         VCC                     5V


       4 Digit Display          Arduino Uno

        GND                      GND

        VCC                      5V

        DIO                      D3

        CLK                      D2


Step 3: Upload Sktetch in ArduinoIDE :
 
You can Download it form here: https://github.com/shubham1008042/Seth


Step 4: Working Of The Project:

In this project i have used arduino uno with ulrasonic sensor(to measure percentage of filled water) and 4 digit seven segment display. The connections of arduino uno with HC-SR04 and 4 digit display is shown in step 2.

The ultrasonic sensor uses sonar to determine the distance to an object. Here’s what happens:
1. The transmitter (trig pin) sends a signal: a high-frequency sound. 

2. When the signal finds an object, it is reflected and… 

3. … the transmitter (echo pin) receives it. 

When ultrasonic sensor detect the level of water trig pin signal reflected back and echo pin of sensor recieves the signal. In my project, the hc-sr04 sensor detect the percentage of water filled in the tank, and show it on the 4 digit seven segment display.

The percentage of water filled is shown by using formula:
                          ((total height of tank-distance of water from sensor)/total   
                                                                                  height of tank)*100
										  
										  
 For code and formulas that i used in this project, you can see it in my sketch as mentioned in step3.


