import dynamixel_sdk as dxl

# Define your Dynamixel motor parameters
baudrate = 115200  
devicename = 'COM16' 

# Initialise the Dynamixel SDK
port_handler = dxl.PortHandler(devicename)
packet_handler = dxl.PacketHandler(1.0)

# Open the serial port
if port_handler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

# Set baudrate
if port_handler.setBaudRate(baudrate):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Set motor speed
def set_speed(motor_id, speed):
    dxl_speed = int(speed * 1023 / 100)  # Convert percentage speed to Dynamixel value
    packet_handler.write2ByteTxRx(port_handler, motor_id, 32, dxl_speed)

# Command motor to move to position
def move_position(motor_id, position):
    packet_handler.write2ByteTxRx(port_handler, motor_id, 30, position)

    
