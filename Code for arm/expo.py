import time
from inverse_kinematics import IK
import serial.tools.list_ports
import serial
from Handtrack import camera_vision
import random
import keyboard


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

    def moveRubbishToBin(self):
        #code will run the camera code then once got something will move it to the home position
        #and release the gripper
        hand = camera_vision(self.speed)
        try:
            IK(hand[0],hand[1],hand[2],self.speed)
        except UnboundLocalError:
            print("shart")
        yes = True

        while yes:
            if keyboard.is_pressed('m'):  
                #move down in z
                moveDown = time.time() + 3
                decrease = 0 
                while (time.time() < moveDown):
                    decrease = decrease + 10
                    IK((hand[0]),(hand[1]),(hand[2] - decrease),10)
            

                #serial communication to tell gripper to grip
                string_to_send = "GRAB" + ';'
                serial_write(string_to_send)          

                #serial communication indicating that gripping has occured
                time.sleep(3)
                #move up in z
                moveUp = time.time() + 3    
                increase = 0 
                while (time.time() < moveUp):
                    increase = increase + 10
                    IK((hand[0]),(hand[1]),(hand[2] + increase),10)
                #move to home position (where bin located) link 2 = 245mm and link 3 = 195mm
                IK(100,400,300,10 ) 

                #serial communication to say to release the gripper
                string_to_send = "NOGRAB" + ';'
                serial_write(string_to_send)
                #back to idle
                if keyboard.is_pressed('c'):  
                    yes = False


class Happy(Behaviour):
    def __init__(self, speed=10, delay=10):
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


        
happy = Happy()
happy.moveRubbishToBin()   