import cv2 as cv
import numpy as np

#Create blank sheet
blank=np.zeros((500,500,3),dtype='uint8')   #uint8 is data type of image
cv.imshow('Blank',blank)

#Create rectanglular patch
blank[250:300, 300:450]=0,255,0
cv.imshow('Green',blank)

#Create Rectangle
cv.rectangle(blank, (0,0) , (blank.shape[1]//3,blank.shape[0]//6) , (0,255,0) , thickness=cv.FILLED)   #thickness=-1 also means same
cv.imshow('Rectangle', blank)                                                                      #blank.shape[1]//3 can be replaced by numerical val of pixel.

#Create Circle
cv.circle(blank , (250,250) , 40 , (0,0,255) , thickness=5)
cv.imshow('Circle',blank)

#Create Line
cv.line(blank , (0,0) , (250,250) , (255,255,255) , thickness=3)
cv.imshow('Line',blank)

#Create Text
cv.putText(blank , 'Hi, Nikshay!!!' , (0,255) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (255,0,0))
cv.imshow('Text',blank)

cv.waitKey(0)