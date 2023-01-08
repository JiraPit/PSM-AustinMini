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

class VectorProcessing:

    def __init__(self,start,end,mid=None) -> None:
        self.__start = start
        self.__mid = mid
        self.__end = end

    def by_angle_All(self) -> Seta:
        v1 = np.array([self.__mid.x,self.__mid.y,self.__mid.z]) - np.array([self.__start.x,self.__start.y,self.__start.z])
        v2 = np.array([self.__mid.x,self.__mid.y,self.__mid.z]) - np.array([self.__end.x,self.__end.y,self.__end.z]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def by_angle_Z(self) -> Seta:
        v1 = np.array([self.__mid.x,self.__mid.y]) - np.array([self.__start.x,self.__start.y])
        v2 = np.array([self.__mid.x,self.__mid.y]) - np.array([self.__end.x,self.__end.y]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def by_angle_X(self) -> Seta:
        v1 = np.array([self.__mid.y,self.__mid.z]) - np.array([self.__start.y,self.__start.z])
        v2 = np.array([self.__mid.y,self.__mid.z]) - np.array([self.__end.y,self.__end.z]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def by_angle_Y(self) -> Seta:
        v1 = np.array([self.__mid.x,self.__mid.z]) - np.array([self.__start.x,self.__start.z])
        v2 = np.array([self.__mid.x,self.__mid.z]) - np.array([self.__end.x,self.__end.z]) 
        seta = acos(np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2))
        return Seta(seta)

    def by_distance_X(self,bounds_original:tuple,bounds_final:tuple,normalize:bool = True) -> float:
        x_distance = float(self.__start.x - self.__end.x)
        return self.__normalize(x=x_distance,bounds_original=bounds_original,bounds_final=bounds_final) if normalize else x_distance

    def by_distance_Y(self,bounds_original:tuple,bounds_final:tuple,normalize:bool = True) -> float:
        y_distance = float(self.__start.y - self.__end.y)
        return self.__normalize(x=y_distance,bounds_original=bounds_original,bounds_final=bounds_final) if normalize else y_distance

    def by_distance_All(self,bounds_original:tuple,bounds_final:tuple,normalize:bool = True) -> float:
        all_distance = sqrt(
            (self.__start.x - self.__end.x)**2 
            + (self.__start.y - self.__end.y)**2 
            + (self.__start.z - self.__end.z)**2
            )
        return self.__normalize(x=all_distance,bounds_original=bounds_original,bounds_final=bounds_final) if normalize else all_distance

    def __normalize (self,x: float, bounds_original: tuple, bounds_final: tuple) -> float:
        x = bounds_final[0] + (x - bounds_original[0]) * (bounds_final[1] - bounds_final[0]) / (bounds_original[1] - bounds_original[0])
        x = min(max(x,bounds_final[0]),bounds_final[1])
        return x




