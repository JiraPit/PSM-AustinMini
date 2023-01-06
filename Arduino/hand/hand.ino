#include <Servo.h>
#include <LinkedList.h>

LinkedList<Servo> servos = LinkedList<Servo>();

void setup() {
  Servo elbow;
  elbow.attach(3);
  servos.add(elbow);

  Servo shoulder_r;
  shoulder_r.attach(4);
  servos.add(shoulder_r);

  Servo shoulder_l;
  shoulder_l.attach(5);
  servos.add(shoulder_l);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String rec = Serial.readStringUntil('$');
    int pin = String(rec[0]).toInt();
    int angle = rec.substring(1).toInt();
    
    servos[pin].write(angle);
  }
}


