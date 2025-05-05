import dynamixel_sdk as dxl  # Import the Dynamixel SDK library

baudrate = 115200  # Baudrate of the motor
devicename = 'COM16'  # Serial port name (change it according to your setup)

# Initialize the Dynamixel SDK
port_handler = dxl.PortHandler(devicename)
packet_handler = dxl.PacketHandler(1.0)

# Initialize GroupSyncWrite instance for setting motor positions and speeds
groupSyncWritePos = dxl.GroupSyncWrite(port_handler, packet_handler, 30, 4)
groupSyncWriteSpeed = dxl.GroupSyncWrite(port_handler, packet_handler, 32, 2)


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
def set_motor_speed(speed):
    """
    Set the speed of all motors.

    Args:
        speed (float): Speed as a percentage (0 to 100).
    """
    groupSyncWriteSpeed.clearParam()
    dxl_speed = int(speed * 1023 / 100)  # Convert percentage speed to Dynamixel value
    speed_bytes = [
        dxl.DXL_LOBYTE(dxl.DXL_LOWORD(dxl_speed)),
        dxl.DXL_HIBYTE(dxl.DXL_LOWORD(dxl_speed)),
        dxl.DXL_LOBYTE(dxl.DXL_HIWORD(dxl_speed)),
        dxl.DXL_HIBYTE(dxl.DXL_HIWORD(dxl_speed))
    ]
    groupSyncWriteSpeed.addParam(1, speed_bytes)
    groupSyncWriteSpeed.addParam(2, speed_bytes)
    groupSyncWriteSpeed.addParam(3, speed_bytes)
    groupSyncWriteSpeed.txPacket()


# Command motor to move to position
def move_to_position(positions):
    """
    Command motors to move to specified positions.

    Args:
        positions (list): List of target positions for each motor.
    """
    position_bytes = [
        [
            dxl.DXL_LOBYTE(dxl.DXL_LOWORD(pos)),
            dxl.DXL_HIBYTE(dxl.DXL_LOWORD(pos)),
            dxl.DXL_LOBYTE(dxl.DXL_HIWORD(pos)),
            dxl.DXL_HIBYTE(dxl.DXL_HIWORD(pos))
        ] for pos in positions
    ]

    # Add Dynamixel goal position value to the Syncwrite parameter storage
    for motor_id, position in enumerate(position_bytes, start=1):
        groupSyncWritePos.addParam(motor_id, position)

    # Syncwrite goal position
    groupSyncWritePos.txPacket()

    finished = False
    while not finished:
        present_positions = [
            packet_handler.read2ByteTxRx(port_handler, motor_id, 36)[0]
            for motor_id in range(1, 4)
        ]
        print(present_positions)
        print(positions)
        finished1 = (present_positions[0] > positions[0] - 10) and (present_positions[0] < positions[0] + 10)
        finished2 = (present_positions[1] > positions[1] - 10) and (present_positions[1] < positions[1] + 10)
        finished3 = (present_positions[2] > positions[2] - 10) and (present_positions[2] < positions[2] + 10)
        print(finished1, finished2, finished3)
        if finished1 and finished2 and finished3:
            finished = True
            # Clear syncwrite parameter storage
            groupSyncWritePos.clearParam()
