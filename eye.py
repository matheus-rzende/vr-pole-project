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
        self.center = None
        self.direction = None
        self.blinked = False

    # Use other face features, or line between horizotal points  
    def vertical(self):
        min_distance = 10000
        min_distance_direction = None
        max_distance = distance(self.up,self.down)
        for direction in [self.up, self.down]:
            dis = distance(self.center, direction)
            if dis < min_distance:
                min_distance = dis
                min_distance_direction = direction
        if min_distance_direction == self.up and min_distance < 0.3*max_distance:
            return 'up'
        if min_distance_direction == self.down and min_distance < 0.3*max_distance:
            return 'down'
        else:
            return None
    
    def horizontal(self):
        min_distance = 10000
        min_distance_direction = None
        max_distance = distance(self.out,self.inner)
        for direction in [self.out, self.inner]:
            dis = distance(self.center, direction)
            if dis < min_distance:
                min_distance = dis
                min_distance_direction = direction
        if min_distance_direction == self.inner:
            if min_distance < 0.5*max_distance:
                return min_distance_direction
        elif min_distance_direction == self.out:
            if min_distance < 0.4*max_distance:
                return min_distance_direction
        else:
            return None
        
    def blink(self): #'Debouncing' necessary, maybe change to horizotal distance between all 5 points or include pupil with less tolerance
        tolerance = 0.15
        max_distance = distance(self.out,self.inner)
        if distance(self.up,self.down) <= tolerance*max_distance and self.blinked == False:
            self.blinked = True
            return True
        else:
            self.blinked = False
            return False


def distance(a,b):
    try:
        return np.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    except TypeError:
        return

      