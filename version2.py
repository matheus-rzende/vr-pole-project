from gtts import gTTS 
from pygame import mixer 
import pygame
import cv2
import numpy as np
import mediapipe as mp
from eye2 import eye
import matplotlib.pyplot as plt
import time
  
#mytext = 'supprimer' 
#language = 'fr' 
#myobj = gTTS(text='a', lang=language, slow=True) 
#myobj.save("a.mp3") 
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (800,300)


mixer.init() 
mixer.music.set_volume(0.7) 

XMAX = 800      
YMAX = 800   
pygame.init()   
screen = pygame.display.set_mode((XMAX,YMAX))  
screen.fill((0,0,0)) 
pygame.display.set_caption('Prototype 2') 
pygame.key.set_repeat(1,50)
my_font_1 = pygame.font.Font('freesansbold.ttf', 50)
my_font_2 = pygame.font.Font('freesansbold.ttf', 200)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

left_eye = eye()
right_eye = eye()

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
current_time = 0
blink_1 = False
music = False
word = ''
music_time = 0

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

    if left_eye.blink() == True and right_eye.blink() == True and blink_1 is False:
      current_time = time.time()
      blink_1 = True

    if blink_1 is True:
        if time.time() - current_time < 1 and time.time() - current_time > 0.2:
            if left_eye.blink() == True and right_eye.blink() == True: 
                blink_1 = False
                if music == False:
                  mixer.music.load("audio.mp3")
                  mixer.music.play()
                  music = True
                elif music == True:
                  music_time = mixer.music.get_pos()/1000 - 3.37
                  if music_time > -3.37 and music_time <= -1.64:
                     word += ' '
                  elif music_time > -1.64 and music_time <= 0:
                     word = word[:-1]
                  elif music_time > 0 and music_time <= 1.08:
                     word += 'a'
                  elif music_time > 1.08 and music_time <= 2.32:
                     word += 'b'
                  elif music_time > 2.32 and music_time <= 3.65:
                     word += 'c'
                  elif music_time > 3.65 and music_time <= 4.88:
                     word += 'd'
                  elif music_time > 4.88 and music_time <= 5.97:
                     word += 'e'
                  elif music_time > 5.97 and music_time <= 7.32:
                     word += 'f'
                  elif music_time > 7.32 and music_time <= 8.63:
                     word += 'g'
                  elif music_time > 8.63 and music_time <= 10.03:
                     word += 'h'
                  elif music_time > 10.03 and music_time <= 11.12:
                     word += 'i'
                  elif music_time > 11.12 and music_time <= 12.40:
                     word += 'j'
                  elif music_time > 12.40 and music_time <= 13.51:
                     word += 'k'
                  elif music_time > 13.51 and music_time <= 14.79:
                     word += 'l'
                  elif music_time > 14.79 and music_time <= 16.05:
                     word += 'm'
                  elif music_time > 16.05 and music_time <= 17.28:
                     word += 'n'
                  elif music_time > 17.28 and music_time <= 18.37:
                     word += 'o'
                  elif music_time > 18.37 and music_time <= 19.52:
                     word += 'p'
                  elif music_time > 19.51 and music_time <= 20.65:
                     word += 'q'
                  elif music_time > 20.65 and music_time <= 21.97:
                     word += 'r'
                  elif music_time > 21.97 and music_time <= 23.38:
                     word += 's'
                  elif music_time > 23.38 and music_time <= 24.51:
                     word += 't'
                  elif music_time > 24.51 and music_time <= 25.58:
                     word += 'u'
                  elif music_time > 25.58 and music_time <= 26.81:
                     word += 'v'
                  elif music_time > 26.81 and music_time <= 28.55:
                     word += 'w'
                  elif music_time > 28.55 and music_time <= 30.00:
                     word += 'x'
                  elif music_time > 30.00 and music_time <= 31.69:
                     word += 'y'
                  elif music_time > 31.69:
                     word += 'z'
                  mixer.music.stop()
                  music = False
        if time.time() - current_time > 1:
           blink_1 = False

    if time.time() - current_time > 5 and music is False and len(word) > 0:
      language = 'fr' 
      myobj = gTTS(text=word, lang=language, slow=True) 
      myobj.save("word.mp3") 
      mixer.music.load("word.mp3")
      mixer.music.play()
      word = ''

    text_surface_1 = my_font_1.render(word, True, (255, 255, 255), (0, 0, 0))  
    screen.fill((0,0,0)) 
    screen.blit(text_surface_1, (10,10))
    pygame.display.update()

    cv2.imshow('Face',cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break

    
cap.release()
