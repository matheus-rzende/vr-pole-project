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
        y_0 = np.mean([self.out[1],self.inner[1]])
        e = y_0 - self.pupil[1] 
        return e - 5
        
    
    def horizontal(self):
        x_0 = np.mean([self.up[0],self.down[0]])
        e = x_0 - self.pupil[0] 
        return e 

    def blink(self): 
        tolerance = 0.2
        max_distance = distance(self.out,self.inner)
        if distance(self.up,self.down) <= tolerance*max_distance:
            self.blinked = True
            return True
        else:
            self.blinked = False
            return False

def distance(a,b):
    return np.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)     