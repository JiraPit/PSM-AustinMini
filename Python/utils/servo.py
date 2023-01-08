import numpy as np
from utils.serial_communication import ArduinoCommunication
from utils.config import Configuration

config = Configuration()

arduino = ArduinoCommunication(port=config.arduino_port,baudrate=9600)
if config.serial_enabled: arduino.connect()

class Servo:
    def __init__(self,
    default_angle: int = 0,
    default_queue: list = [],
    step_legth: int = 5
    ) -> None:
        self.pin = None
        self.angle = default_angle
        self.step_legth = step_legth
        self.queue = default_queue

    def connect(self,pin: int):
        self.pin = pin
        return self

    def __format_data(self,pin:int,angle:int) -> str:
        data = f"{pin}{angle}"
        return data

    def move(self,angle: int) -> None:
        if self.pin == None: print("Please connect to a serial port"); return
        print(f"move {self.pin} from {self.angle} to {angle}")
        arduino.send(self.__format_data(self.pin,angle))
        self.angle = angle

    def queue_steps(self, angle: int) -> None:
        if angle > self.angle:
            steps = np.linspace(self.angle,angle,round((angle-self.angle)/self.step_legth))
        elif angle < self.angle:
            steps = np.flip(np.linspace(angle,self.angle,round((self.angle-angle)/self.step_legth)))
        else: return
        self.queue = steps
    
    def step(self) -> None:
        if len(self.queue) < 2: return
        self.move(self.queue[1])

    

        

        