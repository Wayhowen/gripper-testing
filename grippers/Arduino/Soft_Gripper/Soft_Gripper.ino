#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial btSerial(3, 4);
Servo myservo;

int pos = 90;
int sensorPin = A2;
int sensorValue;
int threshold = 80;
int threshCount = 0;
int gripperDelay = 25;
int baseGripPosition = 0;
int finalGripPosition = 150;

void setup() {
  myservo.attach(7);
  Serial.begin(9600);
  Serial.println("Ready");
  btSerial.begin(9600);
  pinMode(INPUT, A2);
}

void loop() {
  if (btSerial.available() > 0) {
    String action = btSerial.readString();
    if (action == "1") engage();
    else if (action == "0") disengage();
  }

  if (Serial.available()) btSerial.write(Serial.read());
}

void engage() {
  Serial.println("Close");
  for (pos = baseGripPosition; pos <= finalGripPosition; pos += 1) {
    boolean res = pressureSense();
    if(res) break;
    myservo.write(pos);
    delay(gripperDelay);
  }
}

void disengage() {
  Serial.println("Open");
  for (pos; pos >= baseGripPosition; pos -= 1) {
    myservo.write(pos);
    delay(gripperDelay);
  }
}

boolean pressureSense(){
  sensorValue = analogRead(sensorPin);
  if(sensorValue > 0){
    Serial.println(sensorValue);
    delay(5);
  }
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
