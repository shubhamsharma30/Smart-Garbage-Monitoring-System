#include <UbidotsMicroESP8266.h>

#define TOKEN  "A1E-TvDESFa7qD2CibLpVV8a0ORdq4rCni"  // Put here your Ubidots TOKEN
#define WIFISSID "shubzap" // Put here your Wi-Fi SSID
#define PASSWORD "amifool2u" // Put here your Wi-Fi password


const int trigPin =5;
const int echoPin =4;
Ubidots client(TOKEN);

void setup() {
Serial.begin(9600);
client.wifiConnection(WIFISSID, PASSWORD);
//client.setDebug(true); // Uncomment this line to set DEBUG on
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

}
void loop() {

        digitalWrite(trigPin, LOW);
        delayMicroseconds(2);
      
        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
      
        digitalWrite(trigPin, LOW);
        
        float duration = pulseIn(echoPin, HIGH);
        float distance=(duration*0.034)/2;
        Serial.println(distance);
          Serial.print("cm");
        client.add("Distance", distance);
         client.sendAll(true);
        delay(1000);
}
