import serial
import time
import serial.tools.list_ports
import random
import time
from inverse_kinematics import IK

from Handtrack import camera_vision
arduino = serial.Serial(port='COM17', baudrate=115200, timeout=.1)


def serial_write(x):
    arduino.write(x.encode())
    time.sleep(0.05)
    return


class Behaviour:
    def __init__(self, speed=10, delay=10):
        self.name = "Frank"
        self.speed = speed
        self.delay = delay

    def printValues(self):
        print(self.name, self.speed, self.delay)

    def moveRubbishToBin(self):
        # Your existing code for moving rubbish to the bin
        pass


class Happy(Behaviour):
    def __init__(self, speed=10, delay=10):
        super().__init__(speed, delay)


class Sad(Behaviour):
    def __init__(self, speed=50, delay=10):
        super().__init__(speed, delay)


class Nuts(Behaviour):
    def __init__(self, speed=100, delay=10):
        super().__init__(speed, delay)


class Pissed(Behaviour):
    def __init__(self, speed=75, delay=10):
        super().__init__(speed, delay)



