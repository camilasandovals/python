import face_recognition
import cv2
import numpy as np

#This project uses our webcam and tries to detect and, if possible, recognize the faces in view

#To speed things up we will use 1/4 the resolution of the camera and skip every other frame 

video_capture = cv2.VideoCapture(0) #references webcam 0

#Load in our first sample face
todd_image = face_recognition.load_image_file("todd.jpeg")
todd_face_encoding = face_recognition.face_encodings(todd_image)[0]

#Do the same for the second image
damian_image = face_recognition.load_image_file("damian.jpg")
damian_face_encoding = face_recognition.face_encodings(damian_image)[1]

jiho_image = face_recognition.load_image_file("jiho.png")
jiho_face_encoding = face_recognition.face_encodings(jiho_image)[2]
