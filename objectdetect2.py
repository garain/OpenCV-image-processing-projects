# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 00:33:28 2018

@author: garain
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:02:06 2018

@author: garain
"""

# -*- coding: utf-8 -*-
import cv2
import numpy as np
h=2160
w=3920
cap=cv2.VideoCapture(0)
cap.set(3,w)
cap.set(4,h)
while 1:
    _,frame1=cap.read()#The underscore is must before frame for conversion of grey to be functional.
    grey=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    _,th=cv2.threshold(grey,200,255,cv2.THRESH_BINARY)
    laplacian=cv2.Laplacian(th,cv2.CV_8U)
    edges=cv2.Canny(laplacian,150,150)
    c, h=cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,c,-1,(0,0,255),2)                
    cv2.imshow('Detection',frame1)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    


cv2.destroyAllWindows()
cap.release()
           #exit on pressing esc.
