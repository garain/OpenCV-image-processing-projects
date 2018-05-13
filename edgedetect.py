# -*- coding: utf-8 -*-
import cv2
cap=cv2.VideoCapture(0)
h=2160
w=3840
cap.set(3,h)
cap.set(4,w)
while 1:
    _,frame=cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_8U)
    Sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    Sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(laplacian,150,150)
    cv2.imshow('Original', frame)
    cv2.imshow('EdgeDetect',laplacian)
    cv2.imshow('Sobelx',Sobelx)
    cv2.imshow('Sobely',Sobely)
    cv2.imshow('Edges',edges)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
   
   
cv2.destroyAllWindows()
cap.release()
    
    