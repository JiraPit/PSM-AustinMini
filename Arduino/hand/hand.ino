#include <Servo.h>
#include <LinkedList.h>

LinkedList<Servo> servos = LinkedList<Servo>();
char Buf[30];

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
    String pin = String(rec[0]);
    String angle = rec.substring(1);
    
    servos[pin.toInt()].write(angle.toInt());
  }
}


