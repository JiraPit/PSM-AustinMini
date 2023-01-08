import mediapipe as mp
import cv2

from utils.config import Configuration
from utils.servo import Servo
from utils.vector_processing import VectorProcessing

config = Configuration()

#/Camera
CAM = cv2.VideoCapture(config.video_port)

#/Models
MP_POSE = mp.solutions.pose
MP_HANDS = mp.solutions.hands
DRAWER = mp.solutions.drawing_utils
LANDMARKS = mp.solutions.pose.PoseLandmark
POSE_MODEL = MP_POSE.Pose(model_complexity=config.pose_model_complexity)
HANDS_MODEL = MP_HANDS.Hands()

#/Servos
servos = {
    "elbow"         : Servo(default_angle=0,step_legth=10).connect(pin=2),
    "shoulder_right": Servo(default_angle=0,step_legth=5).connect(pin=3),
    "shoulder_left" : Servo(default_angle=0,step_legth=5).connect(pin=4),
    "thumbf"        : Servo(default_angle=0,step_legth=5).connect(pin=5),
    "indexf"        : Servo(default_angle=0,step_legth=5).connect(pin=6),
    "middlef"       : Servo(default_angle=0,step_legth=5).connect(pin=7),
    "ringf"         : Servo(default_angle=0,step_legth=5).connect(pin=8),
    "pinkyf"        : Servo(default_angle=0,step_legth=5).connect(pin=9)
}

while True:
    #get frame
    valid,img = CAM.read()
    if not valid: continue

    #pre-processing
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #processing
    pose_result = POSE_MODEL.process(imgRGB)
    hand_result = HANDS_MODEL.process(imgRGB)

    #post-processing
    if pose_result.pose_world_landmarks:
        pose_landmarks = pose_result.pose_world_landmarks.landmark
        if config.draw: DRAWER.draw_landmarks(img,pose_result.pose_landmarks,MP_POSE.POSE_CONNECTIONS)

        arm_horizontal_angle = VectorProcessing(
            start = pose_landmarks[LANDMARKS.LEFT_WRIST],
            end = pose_landmarks[LANDMARKS.LEFT_SHOULDER]
            ).by_distance_X(
                normalize=True,
                bounds_original=config.elbow_range,
                bounds_final=config.elbow_servo_range)
        servos["elbow"].queue_steps(angle=round(arm_horizontal_angle))

        arm_vertical_angle = VectorProcessing(
            start = pose_landmarks[LANDMARKS.LEFT_WRIST],
            end = pose_landmarks[LANDMARKS.LEFT_ELBOW]
        ).by_distance_Y(
            normalize=True,
            bounds_original=config.shoulder_range,
            bounds_final=config.shoulder_servo_range)
        servos["shoulder_right"].queue_steps(angle=round(arm_vertical_angle))

    if hand_result.multi_hand_world_landmarks:
        hand_landmarks = hand_result.multi_hand_world_landmarks
        hand_landmarks = [hand_landmarks[side] for side in range(len(hand_landmarks)) if hand_result.multi_handedness[side].classification[0].label[0] == "R"]
        if len(hand_landmarks) > 0:
            hand_landmarks = hand_landmarks[0].landmark

            thumbf_angle = VectorProcessing(
                start = hand_landmarks[4],
                end = hand_landmarks[17],
            ).by_distance_All(
                normalize=True,
                bounds_original=config.thumbf_range,
                bounds_final=config.thumbf_servo_range)
            servos["thumbf"].queue_steps(angle=round(thumbf_angle))

            indexf_angle = VectorProcessing(
                start = hand_landmarks[8],
                end = hand_landmarks[0],
            ).by_distance_All(
                normalize=True,
                bounds_original=config.indexf_range,
                bounds_final=config.indexf_servo_range)
            servos["indexf"].queue_steps(angle=round(indexf_angle))
            
            middlef_angle = VectorProcessing(
                start = hand_landmarks[12],
                end = hand_landmarks[0],
            ).by_distance_All(
                normalize=True,
                bounds_original=config.middlef_range,
                bounds_final=config.middlef_servo_range)
            servos["middlef"].queue_steps(angle=round(middlef_angle))
            
            ringf_angle = VectorProcessing(
                start = hand_landmarks[16],
                end = hand_landmarks[0],
            ).by_distance_All(
                normalize=True,
                bounds_original=config.ringf_range,
                bounds_final=config.ringf_servo_range)
            servos["ringf"].queue_steps(angle=round(ringf_angle))
            
            pinkyf_angle = VectorProcessing(
                start = hand_landmarks[20],
                end = hand_landmarks[0],
            ).by_distance_All(
                normalize=True,
                bounds_original=config.pinkyf_range,
                bounds_final=config.pinkyf_servo_range)
            servos["pinkyf"].queue_steps(angle=round(pinkyf_angle))

    for servo in servos.values(): servo.step()

    if config.cv_show:
        cv2.imshow('Result',img)

    if(cv2.waitKey(config.wait_time) & 0xFF == ord('q')):
        break

CAM.release()
cv2.destroyAllWindows()