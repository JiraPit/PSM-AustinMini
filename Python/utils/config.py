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
        self.arduino_port = "COM5"
        self.arduino_port = "/dev/ttyUSB0"

        #arm
        self.elbow_range = (-0.3,0.3)#/
        self.elbow_servo_range = (0,180)
        self.shoulder_range = (-0.18,0.15)#/
        self.shoulder_servo_range = (0,180)

        #hand
        self.thumbf_range = (0,1)
        self.thumbf_servo_range = (0,1)
        self.indexf_range = (0,1)
        self.indexf_servo_range = (0,1)
        self.middlef_range = (0,1)
        self.middlef_servo_range = (0,1)
        self.ringf_range = (0,1)
        self.ringf_servo_range = (0,1)
        self.pinkyf_range = (0,1)
        self.pinkyf_servo_range = (0,1)
        
    