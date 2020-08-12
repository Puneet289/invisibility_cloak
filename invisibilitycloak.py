import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)

bg=0

for i in range(0,50):
    a,bg=cap.read()

while (1):
    b,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    minHSV=np.array([90,50,50])
    maxHSV=np.array([130,255,255])
    
    maskHSV=cv2.inRange(hsv,minHSV,maxHSV)
    
    blurred=cv2.medianBlur(maskHSV,ksize=9)
    inv=cv2.bitwise_not(blurred)
    res=cv2.bitwise_or(frame,frame,mask=inv)
    result=cv2.bitwise_or(bg,bg,mask=blurred)
    final=cv2.bitwise_or(res,result)
    
    cv2.imshow('frame',final)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()