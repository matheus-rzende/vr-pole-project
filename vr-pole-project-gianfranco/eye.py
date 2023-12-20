import cv2
import numpy as np
import mediapipe as mp
import time

class eye(object):

    def __init__(self):
        self.out = [0,0]
        self.inner = [0,0]
        self.up = [0,0]
        self.down = [0,0]
        self.center = [0,0]
        self.direction = None
        self.blinked = False

    # distance_vertical/distance_horizontal = 0.3
    def vertical(self):
        distance_horizontal = distance(self.out,self.inner)
        distance_vertical = distance(self.up,self.down)
        mean_vertical = int(np.mean([self.out[1],self.inner[1]]))
        distance_up = distance(self.up,[self.up[0],mean_vertical])
        if distance_up < 0.15*distance_horizontal and distance_vertical > 0.22*distance_horizontal:
            return self.down
        if distance_up > 0.25*distance_horizontal:
            return self.up
        
    
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


      