import mediapipe as mp
import cv2

from utils.config import Configuration
from utils.servo import Servo
from utils.vector_processing import HandProcessing, ArmProcessing

config = Configuration()

#/Camera
CAM = cv2.VideoCapture(config.VideoPort)

#/Models
MP_POSE = mp.solutions.pose
MP_HANDS = mp.solutions.hands
DRAWER = mp.solutions.drawing_utils
LANDMARKS = mp.solutions.pose.PoseLandmark
POSE_MODEL = MP_POSE.Pose(model_complexity=config.ModelComplexity)
HANDS_MODEL = MP_HANDS.Hands()

#/Servos
servos = {
    "shoulder"  : Servo(default_angle=0,step_legth=5).connect(pin=3),
    "elbow"     : Servo(default_angle=0,step_legth=5).connect(pin=4),
    "thumbf"    : Servo(default_angle=0,step_legth=5).connect(pin=5),
    "indexf"    : Servo(default_angle=0,step_legth=5).connect(pin=6),
    "middlef"   : Servo(default_angle=0,step_legth=5).connect(pin=7),
    "ringf"     : Servo(default_angle=0,step_legth=5).connect(pin=8),
    "pinkyf"    : Servo(default_angle=0,step_legth=5).connect(pin=9)
}

while True:
    #-get frame
    valid,img = CAM.read()
    if not valid: continue

    #-pre-processing
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #-processing
    pose_result = POSE_MODEL.process(imgRGB)
    hand_result = HANDS_MODEL.process(imgRGB)

    #-post-processing
    if pose_result.pose_world_landmarks:
        pose_landmarks = pose_result.pose_world_landmarks.landmark
        if config.draw: DRAWER.draw_landmarks(img,pose_result.pose_landmarks,MP_POSE.POSE_CONNECTIONS)

        elbow_angle = ArmProcessing(
            start = pose_landmarks[LANDMARKS.LEFT_WRIST],
            mid = None,
            end = pose_landmarks[LANDMARKS.LEFT_SHOULDER]
            ).by_distance_X(absolue_max=config.elbow_max)
        # print(elbow_angle) 
        #0.04-0.14
        # servos["elbow"].queue_steps(angle=elbow_angle.degrees)

        shoulder_angle = ArmProcessing(
            start = pose_landmarks[LANDMARKS.LEFT_WRIST],
            mid = None,
            end = pose_landmarks[LANDMARKS.LEFT_ELBOW]
        ).by_distance_Y(absolue_max=config.shoulder_max)
        # print(shoulder_angle)
        # 0.03-0.2
        # servos["shoulder"].queue_steps(angle=elbow_angle.degrees)

    if hand_result.multi_hand_world_landmarks:
        hand_landmarks = hand_result.multi_hand_world_landmarks
        hand_landmarks = [hand_landmarks[side] for side in range(len(hand_landmarks)) if hand_result.multi_handedness[side].classification[0].label[0] == "L"]
        if len(hand_landmarks) > 0:
            pass
    
    for servo in servos.values(): servo.step()

    if config.cv_show:
        cv2.imshow('Result',img)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

CAM.release()
cv2.destroyAllWindows()