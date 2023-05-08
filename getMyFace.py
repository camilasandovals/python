import face_recognition
import cv2
import numpy as np

#This project uses our webcam and tries to detect and, if possible, recognize the faces in view

#To speed things up we will use 1/4 the resolution of the camera and skip every other frame 
