import serial
from utils.config import Configuration

config = Configuration();

class ArduinoCommunication():
    def __init__(self,port: str or int, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate
        self.reciever = None

    def connect(self):
        self.reciever = serial.Serial(port=str(self.port), baudrate=self.baudrate, timeout=1, parity=serial.PARITY_EVEN, stopbits=1)

    def send(self, data:str):
        if (self.reciever == None) or (not config.serial_enabled): return
        try:
            self.reciever.write(bytes(data.replace("\n","").replace("\t","").replace(" ","").replace(",","")+"$",'UTF-8'))
        except Exception as e:
            print(e)