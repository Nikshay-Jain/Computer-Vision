import cv2 as cv

img=cv.imread('Raj.jpg')
gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#Simple Thresholding
ret1,thresh1=cv.threshold(gray , 128 , 255 , cv.THRESH_BINARY)
cv.imshow('Simple Thresholding',thresh1)

#Inverse Thresholding
ret2,thresh2=cv.threshold(gray , 128 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholding',thresh2)

#Adaptive Thresholding
adap=cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 3)
cv.imshow('Adaptive Thresholding',adap)

#Inverse Adaptive Thresholding
adap_inv=cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV , 11 , 3)
cv.imshow('Adaptive Thresholding2',adap_inv)

cv.waitKey(0)