import math
import time
from dynamixel_control_single_motor import move_position, set_speed,packet_handler,port_handler

# lengths of the linkagees
l1 = 160
l2 = 245
l3 = 300



def IK(x,y,z,speed):

    #calculation for the IK
    rSquared = x*x + y*y
    r = math.sqrt(rSquared)
    try:
        theta1 = math.atan2(y, x)

        theta3 = math.acos((rSquared + (z * z) - (l2 * l2) - (l3 * l3)) / (2 * l2 * l3))

        theta2 = math.atan2(-z, r) - math.atan2(l3 * math.sin(theta3), l2 + l3 * math.cos(theta3))
    except ValueError:
        print("fart")

    theta1 = math.degrees(theta1) - 90
    theta2 = math.degrees(theta2) 
    theta3 = math.degrees(theta3) 

    print(theta1,theta2,theta3)

    pos1 = abs(round(theta1 / 0.29))
    pos2 = abs(round(theta2 / 0.29)) + 100
    pos3 = abs(round(theta3 / 0.29)) + 30
    

    if(pos1 < 600 and pos2 < 600 and pos3 < 600):
        
        print(pos1,pos2,pos3)
        positions = [pos1,pos2,pos3]

        # set the speed of each servo
        set_speed(1,speed)
        set_speed(2,speed)
        set_speed(3,speed)

        # send the position to each servo
        move_position(1,positions[0])
        move_position(2,positions[1])
        move_position(3,positions[2])
        #loop that checks if the position has been reached
        finished = False
        while not finished:
            present_positions = [
                packet_handler.read2ByteTxRx(port_handler, motor_id, 36)[0]
                for motor_id in range(1, 4)
            ]
            print(present_positions)
            print(positions)
            finished1 = (present_positions[0] > positions[0] - 60) and (present_positions[0] < positions[0] + 60)
            finished2 = (present_positions[1] > positions[1] - 60) and (present_positions[1] < positions[1] + 60)
            finished3 = (present_positions[2] > positions[2] - 60) and (present_positions[2] < positions[2] + 60)
            print(finished1, finished2, finished3)
            if finished1 and finished2 and finished3:
                finished = True
    else:
        print(pos1,pos2,pos3)
        positions = [pos1,pos2,pos3]


        


    return positions


# yMax = IK(0,l3+l2,0,10)
# xMax = IK(l3+l2,0,0,10)
#homePos = IK(l3,0,l2,10)
# zMax = IK(0,0,l3+l2,10)
# IK(l3,0,l2,10)
# xMax = IK(l3+l2,0,0,10)
# yMax = IK(0,-l3-l2,0,10)
# IK(0,-l2,l3,5)
# IK(l3,0,l2,10)



