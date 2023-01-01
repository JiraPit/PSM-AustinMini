import mediapipe as mp
import cv2

CAM = cv2.VideoCapture(0)
MP_POSE = mp.solutions.pose
MP_HANDS = mp.solutions.hands
DRAW = mp.solutions.drawing_utils
LANDMARKS = mp.solutions.pose.PoseLandmark

POSE_MODEL = MP_POSE.Pose(model_complexity=2)
HAND_MODEL = MP_HANDS.Hands()

CONFIG = {
    "draw" : True
}

while True:
    #-get frame
    validity,img = CAM.read()
    if not validity: continue

    #-pre-processing
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #-processing
    pose_result = POSE_MODEL.process(imgRGB)
    hand_result = HAND_MODEL.process(imgRGB)

    #-pose-processing
    if pose_result.pose_world_landmarks:
        pose_landmarks = pose_result.pose_world_landmarks.landmark
        if CONFIG['draw']:
            DRAW.draw_landmarks(img,pose_result.pose_landmarks,MP_POSE.POSE_CONNECTIONS)
    
    if hand_result.multi_hand_world_landmarks:
        hand_landmarks = hand_result.multi_hand_world_landmarks
        hand_landmarks = [hand_landmarks[side] for side in range(len(hand_landmarks)) if hand_result.multi_handedness[side].classification[0].label[0] == "R"]

        
    cv2.imshow('Result',img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

CAM.release()
cv2.destroyAllWindows()