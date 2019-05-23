# Smart-Garbage-Monitoring-System

Garbage may consist of the unwanted material left over from City, Public area, Society, College, home etc. This project is related to the “Smart City- Clean City” and based on “Internet of Things” (IoT). So for smart lifestyle, cleanliness is needed, and cleanliness is begins with Garbage Bin.This project will help to eradicate or minimize the garbage disposal problem. The Internet of Things ( IoT ) is a recent communication paradigm that envisions near future, in which the objects of everyday life will be equipped with micro-controllers, transceivers for digital communication, and suitable protocol stacks that will make them able to communicate with one another and with the users, becoming an integral part of the Internet. This project IoT Garbage Monitoring system is a very innovative system which will help to keep the cities clean.

This system monitors the garbage bins and informs about the level of garbage collected in the garbage bins via a web page. For this the system uses ultrasonic sensors placed over the bins to detect the garbage level and compare it with the garbage bins depth. The system makes use of Arduino family micro-controller, Wi-Fi modem for sending data. The Web-Applicaton is used to display the status of the level of garbage collected in the bins. Whereas a web page is built to show the status to the user monitoring it. The web page gives a graphical view of the garbage bins and highlights the garbage collected in color in order to show the level of garbage collected. The gauge shows the status of the garbage level. Thus this system helps to keep the city clean by informing about the garbage levels of the bins by providing graphical image of the bins via a web page.

Step 1: Components Required :

You will need the following materials for making your own Water Level Detector

HARDWARE REQUIRED:
                

Ultrasonic Sensor             - HC-SR04                 

Wi-Fi shield                  - Node MCU                

Microcontroller               - Arduino UNO             

Connecting wires              - Jumper wires         


Step 2 : Upload Sketch:

You can get it here:https://github.com/shubham1008042/Smart-Garbage-Monitoring-System/blob/master/ultra_esp/ultra_esp.ino


Step 3 : Working of the Project:


An ultrasonic sensor will be placed on the interior side of the lid, the one facing the solid waste. As trash increases, the distance between the ultrasonic and the trash decreases. This live data will be sent to our micro- controller.

Micro- controller then processes the data and sends to ubidots(cloud) with the help of Wi-Fi module(Node MCU).

Also there is web application for monitoring sensor or control electrical devices via local Wi-Fi or Internet and Control internet of things server - ubidots data monitor.

Web application is in python and will be uploaded soon.
