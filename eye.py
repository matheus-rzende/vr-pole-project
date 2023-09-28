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
        self.more_up = None
        self.more_down = None
        self.direction = None
        self.blinked = False

    # Use other face features, or line between horizotal points  
    def vertical(self):
        min_distance = 10000
        min_distance_direction = None
        max_distance = distance(self.more_up,self.more_down)
        for direction in [self.more_up, self.more_down]:
            dis = distance(self.center, direction)
            if dis < min_distance:
                min_distance = dis
                min_distance_direction = direction
        if min_distance_direction == self.more_up:
            if min_distance < 0.4*max_distance:
                return min_distance_direction
        elif min_distance_direction == self.more_down:
            if min_distance < 0.47*max_distance:
                return min_distance_direction
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
        
    #'Debouncing' necessary, maybe change to horizotal distance between all 5 points 
    def blink(self): 
        tolerance = 0.1
        max_distance = distance(self.out,self.inner)
        if distance(self.up,self.down) <= tolerance*max_distance and self.blinked == False:
            self.blinked = True
            return True
        else:
            self.blinked = False
            return False


def distance(a,b):
    return np.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)


      