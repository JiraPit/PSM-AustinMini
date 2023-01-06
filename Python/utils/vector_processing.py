import numpy as np

from math import sqrt,acos
import numpy as np
import mediapipe as mp

HAND_PARTS = mp.solutions.hands.HandLandmark

class Seta:
    def __init__(self,seta) -> None:
        self.__seta = seta
    
    @property
    def degrees(self):
        return round(np.degrees(self.__seta))

class HandProcessing:
    def __init__(self,hand) -> None:
        self.hand = hand

    def normalized_absolute_vector(self,name:int,ref_point,max:float) -> float:
        landmarks = self.hand.landmark[name]
        AbsoluteVector = sqrt(
            (landmarks.x - ref_point.x)**2 
            + (landmarks.y - ref_point.y)**2 
            + (landmarks.z - ref_point.z)**2
            )
        return AbsoluteVector/max

class ArmProcessing:

    def __init__(self,start,end,mid) -> None:
        self.__start = start
        self.__mid = mid
        self.__end = end

    def around_ALL(self) -> Seta:
        v1 = np.array([self.__mid.x,self.__mid.y,self.__mid.z]) - np.array([self.__start.x,self.__start.y,self.__start.z])
        v2 = np.array([self.__mid.x,self.__mid.y,self.__mid.z]) - np.array([self.__end.x,self.__end.y,self.__end.z]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def around_Z(self) -> Seta:
        v1 = np.array([self.__mid.x,self.__mid.y]) - np.array([self.__start.x,self.__start.y])
        v2 = np.array([self.__mid.x,self.__mid.y]) - np.array([self.__end.x,self.__end.y]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def around_X(self) -> Seta:
        v1 = np.array([self.__mid.y,self.__mid.z]) - np.array([self.__start.y,self.__start.z])
        v2 = np.array([self.__mid.y,self.__mid.z]) - np.array([self.__end.y,self.__end.z]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def around_Y(self) -> Seta:
        v1 = np.array([self.__mid.x,self.__mid.z]) - np.array([self.__start.x,self.__start.z])
        v2 = np.array([self.__mid.x,self.__mid.z]) - np.array([self.__end.x,self.__end.z]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def by_distance_X(self,absolue_max) -> int:
        xDistance = self.__start.x - self.__end.x
        normalized_distance = abs(xDistance)/absolue_max
        return normalized_distance * (xDistance/abs(xDistance))

    def by_distance_Y(self,absolue_max) -> int:
        xDistance = self.__start.y - self.__end.y
        normalized_distance = abs(xDistance)/absolue_max
        return normalized_distance * (xDistance/abs(xDistance))




