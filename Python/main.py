import mediapipe as mp
import cv2

from utils.config import Configuration
from utils.servo import Servo

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
shoulder_servo = Servo(default_angle=0,step_legth=5).connect(pin=3)
elbow_servo = Servo(default_angle=0,step_legth=5).connect(pin=4)
thumbf_servo = Servo(default_angle=0,step_legth=5).connect(pin=5)
indexf_servo = Servo(default_angle=0,step_legth=5).connect(pin=6)
middlef_servo = Servo(default_angle=0,step_legth=5).connect(pin=7)
ringf_servo = Servo(default_angle=0,step_legth=5).connect(pin=8)
pinkyf_servo = Servo(default_angle=0,step_legth=5).connect(pin=9)

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
        elbow_servo.queue_steps(10)
    if hand_result.multi_hand_world_landmarks:
        hand_landmarks = hand_result.multi_hand_world_landmarks
        hand_landmarks = [hand_landmarks[side] for side in range(len(hand_landmarks)) if hand_result.multi_handedness[side].classification[0].label[0] == "R"]

    if config.cv_show:
        cv2.imshow('Result',img)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

CAM.release()
cv2.destroyAllWindows()