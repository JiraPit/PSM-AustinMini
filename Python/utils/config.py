class Configuration:
    def __init__(self) -> None:
        self.VideoPort = 0
        self.ModelComplexity = 2
        self.draw = True
        self.cv_show = True
        self.serial_enabled = False
        self.arduino_port = "COM0"
        #arm
        self.elbow_max = 1
        self.shoulder_max = 1
        #hand
        self.thumbf_range = 1
        self.indexf_range = 1
        self.middlef_range = 1
        self.ringf_range = 1
        self.pinkyf_range = 1
        
    