#include <Servo.h>
#include <LinkedList.h>

// LinkedList<Servo> servos = LinkedList<Servo>();
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;
Servo servo9;
void setup() {
  servo2.attach(2);
  // servos.add(servo2);

  servo3.attach(3);
  // servos.add(servo3);

  servo4.attach(4);
  // servos.add(servo4);

  servo5.attach(5);
  // servos.add(servo5);

  servo6.attach(6);
  // servos.add(servo6);

  servo7.attach(7);
  // servos.add(servo7);

  servo8.attach(8);
  // servos.add(servo8);

  servo9.attach(9);
  // servos.add(servo9);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String rec = Serial.readStringUntil('$');
    Serial.println(rec);
    int pin = String(rec[0]).toInt();
    int angle = rec.substring(1).toInt();
    Serial.println(pin);
    Serial.println(angle);
    switch(pin){
      case 2:
        servo2.write(angle);
        break;
      case 3:
        servo3.write(angle);
        break;
      case 4:
        servo4.write(angle);
        break;
      case 5:
        servo5.write(angle);
        break;
      case 6:
        servo6.write(angle);
        break;
      case 7:
        servo7.write(angle);
        break;
      case 8:
        servo8.write(angle);
        break;
      case 9:
        servo9.write(angle);
        break;
    }
  }
}


