# -*- coding: utf-8 -*-
import cv2
import numpy as np
h=1080
w=1920
cap=cv2.VideoCapture(0)
cap.set(3,w)
cap.set(4,h)
while 1:#This part of reading frame1 and frame2 must be below while 1:
    _,frame1=cap.read()#The underscore is must before frame for conversion of grey to be functional.
    _,frame2=cap.read()
    d=cv2.absdiff(frame1,frame2)
    grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(5,5),0)
    _,th=cv2.threshold(blur,50,255,cv2.THRESH_BINARY)
    laplacian=cv2.Laplacian(th,cv2.CV_8U)
    edges=cv2.Canny(laplacian,150,150)
    c, h=cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,c,-1,(0,0,255),2)
    cv2.imshow('Original',frame2)
    cv2.imshow('Detection',frame1)
    cv2.imshow('Canny',edges)
    cv2.imshow('Laplacian',laplacian)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
    
frame1=frame2
ret,frame2=cap.read()


cv2.destroyAllWindows()
cap.release()
           #exit on pressing esc.
