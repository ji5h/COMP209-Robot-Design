import cv2
import mediapipe as mp
import time
import math              
from inverse_kinematics import IK
import keyboard



def camera_vision(speed):
    # Initialize MediaPipe Hand model
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)

    # Open webcam
    cap = cv2.VideoCapture(1)

    rows, cols = 10, 10
    grid_color = (255, 255, 255)  # White color
    thickness = 1
    locked = False
    print(locked)
    yes = True

    testTime = time.time() + 30
    while yes:

        if keyboard.is_pressed('space'):  
            yes = False

        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands
        results = hands.process(rgb_frame)

        draw_grid(frame, rows, cols, grid_color, thickness)
        
        # If hand(s) detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Calculate bounding box
                bBox = calc_bounding_box(hand_landmarks, frame)

                # Draw bounding box
                cv2.rectangle(frame, (bBox[0], bBox[1]), (bBox[                                 2], bBox[3]), (255, 0, 0), 2)

                # Calculate center of bounding box
                center_x = int((bBox[0] + bBox[2]) / 2)
                center_y = int((bBox[1] + bBox[3]) / 2)

                box_width = bBox[2] - bBox[0]
                box_height = bBox[3] - bBox[1]

                cv2.circle(frame, (center_x, center_y), 5, (0, 255, 255), -1)

                #----------------
                height, width = frame.shape[:2]

                xratio = center_x*10/width
                yratio = center_y*10/height
                xratio = xratio - 5
                xratio = xratio*-1

                xratio = xratio * 90 #100
                yratio = yratio * 65 #65

                print(yratio, xratio, 0)
                try:
                    IK(yratio,xratio,100,speed)
                except UnboundLocalError:
                    print("shart")
                label = f"{xratio, yratio} coords"  # Customize the label as needed
                cv2.putText(frame, label, (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Display output
        cv2.imshow('Hand Tracking', frame)

        # Break the loop on 'q' key press
        key = cv2.waitKey(1)
        if key == ord('q'):
            break




    # Release resources
    #
    cap.release()
    cv2.destroyAllWindows()
    return yratio, xratio, 100



def draw_grid(frame, rows, cols, color, thickness):
    for i in range(1, rows):
        cv2.line(frame, (0, i * frame.shape[0] // rows), (frame.shape[1], i * frame.shape[0] // rows), color, thickness)
    for j in range(1, cols):
        cv2.line(frame, (j * frame.shape[1] // cols, 0), (j * frame.shape[1] // cols, frame.shape[0]), color, thickness)

def calc_bounding_box(hand_landmarks, frame):
    # Get image dimensions
    h, w, _ = frame.shape

    # Initialize bounding box coordinates
    x_min, y_min, x_max, y_max = w, h, 0, 0

    # Calculate bounding box coordinates
    for landmark in hand_landmarks.landmark:
        x, y = int(landmark.x * w), int(landmark.y * h)
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    return x_min, y_min, x_max, y_max 

