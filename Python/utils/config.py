class Configuration:
    def __init__(self) -> None:
        #cv2
        self.wait_time = 1

        #mediapipe
        self.video_port = 0
        self.pose_model_complexity = 2
        self.draw = True
        self.cv_show = True

        #arduino_serial
        self.serial_enabled = True
        self.arduino_port = "COM3"
        #self.arduino_port = "/dev/ttyUSB0"

        #arm
        self.elbow_range = (-0.3,0.3)
        self.elbow_servo_range = (45,135)
        self.shoulder_range = (-0.18,0.15)
        self.shoulder_servo_range = (60,150)

        #hands
        self.thumbf_range = (0.05,0.12)
        self.thumbf_servo_range = (40,150)
        self.indexf_range = (0.07,0.15)
        self.indexf_servo_range = (40,150)
        self.middlef_range = (0.06,0.18)
        self.middlef_servo_range = (40,150)
        self.ringf_range = (0.07,0.17)
        self.ringf_servo_range = (40,150)
        self.pinkyf_range = (0.06,0.14)
        self.pinkyf_servo_range = (40,150)
        
    