import numpy as np
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# seleccting capturing device
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.75, min_tracking_confidence=0.75) as holistic:

# device is on or connected to a device then we intialize loop
 while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=2.5, fy=2, )

   #we change color space 2 times for rendering the image 
    # Our operations on the frame come here
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = holistic.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # # # Draw face landmarks

    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS, mp_drawing.DrawingSpec(color=(
         255, 255, 255), thickness=2, circle_radius=1), mp_drawing.DrawingSpec(color=(204, 0, 0), thickness=2, circle_radius=1))


    #  # Right hand
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                               mp_drawing.DrawingSpec(color=(127, 0, 255), thickness=2, circle_radius=4), mp_drawing.DrawingSpec(color=(255, 178, 102), thickness=2, circle_radius=2))

    # #  # Left Hand
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, mp_drawing.DrawingSpec(
        color=(127, 0, 255), thickness=2, circle_radius=4), mp_drawing.DrawingSpec(color=(255, 178, 102), thickness=2, circle_radius=2))

    # # # Pose Detections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(
        0, 0,  255), thickness=2, circle_radius=2), mp_drawing.DrawingSpec(color=(255, 255, 153), thickness=2, circle_radius=2))
 
    
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
