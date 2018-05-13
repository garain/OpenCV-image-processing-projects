# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 23:04:51 2018

@author: garain
"""

import cv2

'''
Face Detector 2: Detects face/faces in frames(webcam)
classifier: haarcascade_frontalface_default.xml from OpenCV library
'''

# load classifier
faceCascade = cv2.CascadeClassifier('/home/garain/Downloads/classifiers/lbpcascade_frontalface_improved.xml')
eyeCascade=cv2.CascadeClassifier('/home/garain/Downloads/classifiers/haarcascade_eye.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    _, frame = video_capture.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eyeCascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()