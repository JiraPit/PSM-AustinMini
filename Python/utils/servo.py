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
    step_legth: int = 5, 
    step_counter: int = 0) -> None:
        self.pin = None
        self.angle = default_angle
        self.step_legth = step_legth
        self.queue = default_queue
        self.step_counter = step_counter

    def connect(self,pin: str):
        self.pin = pin
        return self

    def _format_data(pin:int,angle:int) -> str:
        data = f"{pin},{angle}"
        print(data)
        return data

    def move(self,angle: int) -> None:
        if self.pin == None: print("Please connect to a serial port"); return
        arduino.send(self._format_data(self.pin,angle))
        self.angle = angle

    def queue_steps(self, angle: int) -> None:
        if angle > self.angle:
            steps = np.linspace(self.angle,angle,round((angle-self.angle)/self.step_legth))
        elif angle < self.angle:
            steps = np.linspace(angle,self.angle,round((self.angle-angle)/self.step_legth))
        else: return
        self.queue = steps 
        self.step_counter = 0
    
    def step(self) -> None:
        if len(self.queue) < 1: return
        self.move(self.queue[self.step_counter])
        self.step_counter += 1

    

        

        