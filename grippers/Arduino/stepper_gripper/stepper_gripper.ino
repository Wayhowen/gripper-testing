#include <SoftwareSerial.h>
#include <Stepper.h>


const int stepsPerRevolution = 200;
const int distance = 35;
const int pace = 600;

SoftwareSerial btSerial(3, 4);
Stepper myStepper(stepsPerRevolution, 5, 6);


void setup() {
  myStepper.setSpeed(pace);
  Serial.begin(9600);
  Serial.println("Ready");
  btSerial.begin(9600);
}

void loop() {
  if (btSerial.available() > 0) {
    String action = btSerial.readString();
    if (action == "1") extend(distance);
    else if (action == "0") retract(distance);
  }

  if (Serial.available()) btSerial.write(Serial.read());
}

void retract(int rounds) {
  for(int r = 0; r < rounds; r++){
    Serial.println("clockwise");
    myStepper.step(stepsPerRevolution);
    //delay(500);
  }
}

void extend(int rounds) {
  for(int r = 0; r < rounds; r++){
    Serial.println("counterclockwise");
    myStepper.step(-stepsPerRevolution);
    //delay(500);
  }
}
