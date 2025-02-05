import cv2 as cv
import numpy as np

#Resize     x-->Right   y-->Down    -ve accordingly
img=cv.imread('4K.jpg')
w=img.shape[1]//4
h=img.shape[0]//4
img=cv.resize(img, (w,h), interpolation = cv.INTER_AREA)
blank = np.zeros(img.shape , dtype='uint8')

#Gray then Blur
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Thresholding
ret,thresh=cv.threshold(blur,125,255,cv.THRESH_BINARY)    #ret = 125.0
cv.imshow('Thresh',thresh)

#Casscading
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours),' found!!!')
cv.drawContours(blank , contours , -1 , (0,0,255) , 1)
cv.imshow('Contours' , blank)

cv.waitKey(0)