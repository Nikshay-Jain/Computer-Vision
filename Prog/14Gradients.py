import cv2 as cv
import numpy as np

img=cv.imread('Siberian Tiger.jpg')
cv.imshow('Original',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx=cv.Sobel(gray , cv.CV_64F , 1 , 0)
sobely=cv.Sobel(gray , cv.CV_64F , 0 , 1)
sobelcomb=cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Sobel',sobelcomb)

canny=cv.Canny(gray , 150 , 175)    #itself uses Sobel so used most
cv.imshow('Canny',canny)

cv.waitKey(0)