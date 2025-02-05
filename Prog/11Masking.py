import cv2 as cv
import numpy as np

img=cv.imread('Large.jpg')
blank=np.zeros(img.shape[:2] , dtype='uint8')

mask1=cv.circle(blank.copy() , (img.shape[1]//2 -50 , img.shape[0]//2 -50) , 200 , 255 , -1)
mask2=cv.rectangle(blank.copy() , (420 , 125) , (750 , 500) , 255 , -1)
mask3=cv.bitwise_and(mask1,mask2)
mask4=cv.bitwise_or(mask1,mask2)

masked1=cv.bitwise_and(img,img,mask=mask1)
cv.imshow('Masked1',masked1)

masked2=cv.bitwise_and(img,img,mask=mask2)
cv.imshow('Masked2',masked2)

masked3=cv.bitwise_and(img,img,mask=mask3)
cv.imshow('Masked3',masked3)

masked4=cv.bitwise_and(img,img,mask=mask4)
cv.imshow('Masked4',masked4)

cv.waitKey(0)