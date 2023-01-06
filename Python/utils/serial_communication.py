import serial
from utils.config import Configuration

config = Configuration();

class ArduinoCommunication():
    def __init__(self,port: str or int, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate
        self.reciever = None

    def connect(self):
        self.reciever = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=1, parity=serial.PARITY_EVEN, stopbits=1)

    def send(self, data:str):
        if self.reciever == None: return
        if config.serial_enabled:
            self.reciever.write(bytes(data.replace("\n","").replace("\t","").replace(" ","").replace(",",""),'UTF-8'))