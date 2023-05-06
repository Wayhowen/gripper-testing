#include <SoftwareSerial.h>
#include<Servo.h>

SoftwareSerial btSerial(3, 4);
Servo myservo;
int pos = 0;
int sensorPin = A2;
int sensorValue;
int threshold = 80;
int threshCount = 0;
int gripperDelay = 25;
int baseGripPosition = 80;

void setup() {
  myservo.attach(7);
  Serial.begin(9600);
  Serial.println("Ready");
  btSerial.begin(9600);
  pinMode(INPUT, A2);
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
  //long start = millis();
  //Serial.println("Engaging payload");
  for (pos = baseGripPosition; pos <= 180; pos += 1) {
    boolean res = pressureSense();
    if(res) break;
    myservo.write(pos);
    delay(gripperDelay);
  }
  //Serial.println(millis()-start);
}

void disengage(){
  //long start = millis();
  //Serial.println("Disengaging payload");
  myservo.write(baseGripPosition);
  //while(myservo.read() > 0){}
  //Serial.println(millis()-start);
  
}

boolean pressureSense(){
  sensorValue = analogRead(sensorPin);
  /*if(sensorValue > 0){
    Serial.println(sensorValue);
    delay(5);
  }*/
  if(sensorValue > threshold){
      threshCount++;
      Serial.println(threshCount);
      delay(5);
      if(threshCount > 2){
        int stopPos = myservo.read();
        myservo.write(stopPos);
        Serial.println("CONTACT");
        delay(gripperDelay);
        return true;
      }
  } else{
      threshCount = 0;
  }
  return false;
}
