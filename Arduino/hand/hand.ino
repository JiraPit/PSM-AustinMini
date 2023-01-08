#include <Servo.h>
#include <LinkedList.h>

LinkedList<Servo> servos = LinkedList<Servo>();

void setup() {
  Servo servo2;
  servo2.attach(2);
  servos.add(servo2);

  Servo servo3;
  servo3.attach(3);
  servos.add(servo3);

  Servo servo4;
  servo4.attach(4);
  servos.add(servo4);

  Servo servo5;
  servo5.attach(5);
  servos.add(servo5);

  Servo servo6;
  servo6.attach(6);
  servos.add(servo6);

  Servo servo7;
  servo7.attach(7);
  servos.add(servo7);

  Servo servo8;
  servo8.attach(8);
  servos.add(servo8);

  Servo servo9;
  servo9.attach(9);
  servos.add(servo9);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String rec = Serial.readStringUntil('$');
    int pin = String(rec[0]).toInt()-2;
    int angle = rec.substring(1).toInt();
    servos[pin].write(angle);
  }
}


