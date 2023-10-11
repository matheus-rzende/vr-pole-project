import cv2
import numpy as np
import mediapipe as mp
from eye2 import eye
import pyautogui
import sys
import matplotlib.pyplot as plt
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

screen_w, screen_h = pyautogui.size()

lista1 = list()
lista2 = list()
lista3 = list()

cum_e = 0
previous_time = 0
previous_e = 0

# Edit from here #

left_eye = eye()
right_eye = eye()

point = [640/2,480/2]

#################################
### Face Mesh from Media Pipe ###
#################################
# Don't change

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    height, width, _ = image.shape

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
            pass
      
  #################################
  # Edit frome here #

    current_time = time.time()
        
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

    K = 0.01
    Kp = 8
    Kd = 0.05
    Ki = 0

    t = current_time - previous_time
    
    #if len(lista3) <= 1:
    #  lista3.append(point[0])
    #else:
    #  lista3 = lista3[1:]
    #  lista3.append(point[0])

    #avg = np.mean(lista3)*K

    e = right_eye.horizontal() - point[0]*K
    cum_e += e * t
    rate_e = (e - previous_e)/t

    point[0] += Kp*e + Kd*rate_e + Ki*cum_e

    if point[0] <= 0:
      point[0] = 0
    if point[0] >= width:
      point[0] = width
    if point[1] <= 0:
      point[1] = 0
    if point[1] >= height:
      point[1] = height


    #cv2.circle(image, (point[0],point[1]), 5, color, -1)    

    pyautogui.moveTo(screen_w / width * point[0],screen_h / height * point[1])
      
    #################################
    # Don't edit
    cv2.imshow('Face',cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break

    if cv2.getWindowProperty('Face', cv2.WND_PROP_VISIBLE) <1:
      break

    k = cv2.waitKey(33)
    if k==27:    
        break
    
    lista1.append(right_eye.horizontal())
    lista2.append(point[0]*K)

    previous_e = e
    previous_time = current_time
    
cap.release()

x = np.linspace(0, len(lista1), num=len(lista1))
fig, ax = plt.subplots(1,1,figsize=(20, 8))
ax.plot(x, lista1, color='b',  linewidth=1)
ax.plot(x, lista2, color='r',  linewidth=1)
plt.show()