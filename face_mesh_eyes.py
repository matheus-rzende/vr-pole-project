import cv2
import numpy as np
import mediapipe as mp
from eye import eye
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# Edit from here #

left_eye = eye()
right_eye = eye()

point = [200,200]
color = (np.random.randint(255),np.random.randint(255),np.random.randint(255))

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
        
    right_eye.out = [int(face_landmarks.landmark[33].x*width),int(face_landmarks.landmark[33].y*height)]
    right_eye.inner = [int(face_landmarks.landmark[133].x*width),int(face_landmarks.landmark[133].y*height)]
    right_eye.up = [int(face_landmarks.landmark[159].x*width),int(face_landmarks.landmark[159].y*height)]
    right_eye.down = [int(face_landmarks.landmark[145].x*width),int(face_landmarks.landmark[145].y*height)]
    right_eye.more_up = [int(face_landmarks.landmark[27].x*width),int(face_landmarks.landmark[27].y*height)]
    right_eye.more_down = [int(face_landmarks.landmark[23].x*width),int(face_landmarks.landmark[23].y*height)]
    right_eye.center = [int(face_landmarks.landmark[468].x*width),int(face_landmarks.landmark[468].y*height)]

    left_eye.out = [int(face_landmarks.landmark[263].x*width),int(face_landmarks.landmark[263].y*height)]
    left_eye.inner = [int(face_landmarks.landmark[362].x*width),int(face_landmarks.landmark[362].y*height)]
    left_eye.up = [int(face_landmarks.landmark[386].x*width),int(face_landmarks.landmark[386].y*height)]
    left_eye.down = [int(face_landmarks.landmark[374].x*width),int(face_landmarks.landmark[374].y*height)]
    left_eye.more_up = [int(face_landmarks.landmark[257].x*width),int(face_landmarks.landmark[257].y*height)]
    left_eye.more_down = [int(face_landmarks.landmark[253].x*width),int(face_landmarks.landmark[253].y*height)]
    left_eye.center = [int(face_landmarks.landmark[473].x*width),int(face_landmarks.landmark[473].y*height)]

    cv2.circle(image, (right_eye.out[0],right_eye.out[1]), 2, (0, 0, 255), -1)
    cv2.circle(image, (right_eye.inner[0],right_eye.inner[1]), 2, (0, 0, 255), -1)
    cv2.circle(image, (right_eye.up[0],right_eye.up[1]), 2, (0, 0, 255), -1)
    cv2.circle(image, (right_eye.down[0],right_eye.down[1]), 2, (0, 0, 255), -1)
    cv2.circle(image, (right_eye.center[0],right_eye.center[1]), 2, (0, 0, 255), -1)

    cv2.circle(image, (left_eye.out[0],left_eye.out[1]), 2, (0, 255, 0), -1)
    cv2.circle(image, (left_eye.inner[0],left_eye.inner[1]), 2, (0, 255, 0), -1)
    cv2.circle(image, (left_eye.up[0],left_eye.up[1]), 2, (0, 255, 0), -1)
    cv2.circle(image, (left_eye.down[0],left_eye.down[1]), 2, (0, 255, 0), -1)
    cv2.circle(image, (left_eye.center[0],left_eye.center[1]), 2, (0, 255, 0), -1) 

    if right_eye.horizontal() == right_eye.out and left_eye.horizontal() == left_eye.inner:
       point[0] -= 2
    elif right_eye.horizontal() == right_eye.inner and left_eye.horizontal() == left_eye.out:
       point[0] += 2

    if right_eye.vertical() == right_eye.more_up:
       point[1] -= 2
       print('up')
    elif right_eye.vertical() == right_eye.more_up:
       point[1] += 2
       print('down')

    if left_eye.blink() == True and right_eye.blink() == True:
      color = (np.random.randint(255),np.random.randint(255),np.random.randint(255))

    cv2.circle(image, (point[0],point[1]), 5, color, -1)    

    #################################
    # Don't edit
    cv2.imshow('Face', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break

    if cv2.getWindowProperty('Face', cv2.WND_PROP_VISIBLE) <1:
      break
    
cap.release()