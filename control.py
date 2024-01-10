import cv2
import numpy as np
import mediapipe as mp
from eye2 import eye
import pyautogui
import sys
import matplotlib.pyplot as plt
import time

# Recommended distance 30 cm

# Initializing Face Mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

screen_w, screen_h = pyautogui.size() # Size of whole screen

# Error for control
cum_ex = 0
previous_time = time.time()
previous_ex = 0

# Initializing eye class, for each eye
left_eye = eye()
right_eye = eye()

list1= list()
list2 = list()

# Opening camera and applying the Face Mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)

height, width = int(cap.get(4)), int(cap.get(3)) # Size of image

# Initial position of pointer
point = [width/2,height/2]

# Control constants
Kx = 5.5/320
Kpx = 8
Kdx = 0
Kix = 0

f = 0

mean_x_1 = 0

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()

    # Create image with landmarcks
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # Size of image (different than screen)
    height, width, _ = image.shape

    # Draw the face mesh annotations on the image
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
            pass
      
    # Time for control
    current_time = time.time()
        
    #Right and left eye landmarks
    right_eye.out = [int(face_landmarks.landmark[33].x*width),int(face_landmarks.landmark[33].y*height)]
    right_eye.inner = [int(face_landmarks.landmark[133].x*width),int(face_landmarks.landmark[133].y*height)]
    right_eye.up = [int(face_landmarks.landmark[159].x*width),int(face_landmarks.landmark[159].y*height)]
    right_eye.down = [int(face_landmarks.landmark[145].x*width),int(face_landmarks.landmark[145].y*height)]
    right_eye.pupil = [int(face_landmarks.landmark[468].x*width),int(face_landmarks.landmark[468].y*height)]

    left_eye.out = [int(face_landmarks.landmark[263].x*width),int(face_landmarks.landmark[263].y*height)]
    left_eye.inner = [int(face_landmarks.landmark[362].x*width),int(face_landmarks.landmark[362].y*height)]
    left_eye.up = [int(face_landmarks.landmark[386].x*width),int(face_landmarks.landmark[386].y*height)]
    left_eye.down = [int(face_landmarks.landmark[374].x*width),int(face_landmarks.landmark[374].y*height)]
    left_eye.pupil = [int(face_landmarks.landmark[473].x*width),int(face_landmarks.landmark[473].y*height)]

    # If blink with bothe yes then click
    if left_eye.blink() == True and right_eye.blink() == True:
      pyautogui.click()
    else:
      # Delta time for control
      t = current_time - previous_time

      # Variables to normalize positions
      mean_x = np.mean([right_eye.horizontal(),left_eye.horizontal()])
      point_x = (point[0]-width/2)*Kx
      print(point_x, mean_x)
      if abs(mean_x-mean_x_1) < 1:
        mean_x = mean_x_1

      # Errors
      e_x = mean_x - point_x
      cum_ex += e_x * t
      rate_ex = (e_x - previous_ex)/t

      # PID Control
      point[0] += Kpx*e_x + Kdx*rate_ex + Kix*cum_ex

      mean_x_1 = mean_x

      # Limits to pointer position
      if point_x <= -width/2:
        point_x = -width/2
      if point_x >= width/2:
        point_x = width/2
      if point[0] <= 0:
        point[0] = 0
      if point[0] >= width:
        point[0] = width
      if point[1] <= 0:
        point[1] = 0
      if point[1] >= height:
        point[1] = height

      # Define pointer as the mouse
      pyautogui.moveTo(screen_w / width * point[0], screen_h / height * point[1])

      # Tracking previous step for control
      previous_ex = e_x
      previous_time = current_time
      list1.append(mean_x)
      list2.append(point_x)

    # Necessary for camera opening
    if cv2.waitKey(5) & 0xFF == 27:
      break

    if len(list1) == 100:
      break
    
cap.release()

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1,figsize=(12, 12))
ax.plot(np.arange(len(list1)),list1, color='r', label='Mean')
ax.plot(np.arange(len(list2)),list2, color='b', label='Point')
plt.show()