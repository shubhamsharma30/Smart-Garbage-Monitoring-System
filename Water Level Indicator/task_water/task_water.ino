
#include <TM1637Display.h>

const int CLK = 2; //Set the CLK pin connection to the display
const int DIO = 3; //Set the DIO pin connection to the display
const int trigPin = 8;
const int echoPin = 9;
long duration;
float distance;
float percentage;
const int gap=2;
const int height=12;

TM1637Display display(CLK, DIO);  //set up the 4-Digit Display.

void setup ()
{
  display.setBrightness(0x0a);  //set the diplay to maximum brightness
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}


void loop()
{ 
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
  
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
  
    digitalWrite(trigPin, LOW); 
    duration = pulseIn(echoPin, HIGH); 
  
  // Calculating distance
  distance=(duration/2)/29.1;
  //distance= duration*0.0343/2; 
  Serial.print("Distance = ");
  Serial.print(distance); 
  Serial.println(" cm");
  percentage=(((height+gap)-distance)/height)*100;
  Serial.print("Percentage=");
  Serial.print(percentage);
  Serial.println("%");

 display.showNumberDec(percentage); //Display the Variable value;

if(percentage<=0)
{
  display.showNumberDec(0);
}

if(percentage>=100)
{
   display.showNumberDec(100); 
}
delay(2000);
}
