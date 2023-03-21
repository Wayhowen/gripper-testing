#include <SoftwareSerial.h>
#include<Servo.h>

SoftwareSerial btSerial(3, 4);
Servo myservo;

void setup() {
  myservo.attach(7);
  Serial.begin(9600);
  Serial.println("Ready");
  btSerial.begin(9600);
}

void loop() {
  if (btSerial.available()>0) {
    String action = btSerial.readString();
    if(action == "1") engage();
    else if(action == "0") disengage();
  }

  if (Serial.available()) btSerial.write(Serial.read());
}

void engage(){
  myservo.write(0);
}

void disengage(){
  myservo.write(170);
  
}
