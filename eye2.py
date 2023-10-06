import cv2
import numpy as np
import mediapipe as mp
import time

class eye(object):

    def __init__(self):
        self.out = None
        self.inner = None
        self.up = None
        self.down = None
        self.pupil = None
        self.direction = None
        self.blinked = False

    # distance_vertical/distance_horizontal = 0.3
    def vertical(self):
        pass
        
    
    def horizontal(self):
        max_distance = distance(self.out,self.inner)
        x_0 = np.mean([self.out[0],self.inner[0]])
        e = x_0 - self.pupil[0]
        return e, max_distance


    def blink(self): 
        pass


def distance(a,b):
    return np.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)


      