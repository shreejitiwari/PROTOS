import mediapipe as mp
import cv2
import numpy as np


def x_coordinates(landmark):
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split("\n")[0].split(" ")[1])

def y_coordinates(landmark):
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split("\n")[1].split(" ")[1])

def z_coordinates(landmark):
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split("\n")[2].split(" ")[1])


def orientation():
    x0 = x_coordinates(0)
    y0 = y_coordinates(0)

    x9 = x_coordinates(9)
    y9 = y_coordinates(9)

    if abs(x9 - x0) < 0.001:
        m = 10000000000

    else:
        m = abs((y9-y0)/(x9-x0))
        
        if m>=0 and m<=1:
            if x9>x0:
                return "Right"
            else:
                return "Left"
        
        if m>1:
            if y9>y0:
                return "Down"
            else:
                return "Up"
        


web_cam = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils

with mp_hands.Hands(min_detection_confidence = 0.5,min_tracking_confidence = 0.5, max_num_hands=2) as hands:
    while web_cam.isOpened():
        success, img = web_cam.read()
        image = img.copy()

        if not success:
            print("Ignoring empy camera frame.")
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  
        cv2.imshow('Detecting Hands', image)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mpdraw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mpdraw.DrawingSpec(color=(0,0,255), thickness=3), mpdraw.DrawingSpec(color=(0,255,0)))
                cv2.putText(image, str(orientation()), (250,100), cv2.FONT_HERSHEY_SIMPLEX,1,(200, 100, 255),2)
                cv2.imshow('Detecting Hands', image)
                
        if cv2.waitKey(1)  == ord("q"):
            break
        web_cam.release
