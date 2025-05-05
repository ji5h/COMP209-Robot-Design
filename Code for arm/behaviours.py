import time
from inverse_kinematics import IK
import serial.tools.list_ports
import serial                                                                                       
#from Handtrack import camera_vision
import random
import keyboard

grabState = "NO"

arduino = serial.Serial(port='COM14', baudrate=115200, timeout=.1)

def serial_write(x):
    arduino.write(x.encode())
    time.sleep(0.05)
    return

ports = serial.tools.list_ports.comports()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
serialInst = serial.Serial()

portsList = []


class Behaviour:
    def __init__(self,speed = 10, delay=10):
        self.name = "Frank"
        self.speed = speed
        self.delay = delay
    
    def printValues(self):
        print(self.name,self.speed, self.delay)

    
    def grip(self): 
        while 1:
            if keyboard.is_pressed('space'):  
                string_to_send = "GRAB" + ';'
                serial_write(string_to_send)
                time.sleep(5)
            else:
                string_to_send = "NOGRAB" + ';'
                serial_write(string_to_send)
                time.sleep(1)                                                                                                                                                                                                                                                                                         



class Happy(Behaviour):
    def __init__(self, speed=15, delay=10):
        super().__init__(speed, delay)

class sad(Behaviour):
    def __init__(self, speed=10, delay=10):
        super().__init__(speed, delay)

class nuts(Behaviour):
    def __init__(self, speed=50, delay=10):
        super().__init__(speed, delay)
class pissed(Behaviour):
    def __init__(self, speed=30, delay=10):
        super().__init__(speed, delay)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

# List of available behaviors
behaviors = [Happy()]

# Randomly choose a behavior from the list
selected_behavior = random.choice(behaviors)
selected_behavior.printValues()
#selected_behavior.moveRubbishToBin() 
selected_behavior.grip()
