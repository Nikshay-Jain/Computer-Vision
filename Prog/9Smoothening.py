import cv2 as cv

img=cv.imread('Raj.jpg')

#Average - div img in 3x3 grid and averages each block
avg=cv.blur(img, (3,3))
cv.imshow('Avg',avg)

#Gaussian
gauss=cv.GaussianBlur(img, (3,3) , 0)
cv.imshow('Gaussian',gauss)

#Median
med=cv.medianBlur(img,3)
cv.imshow('Median',med)

#Bilateral - keeps edges sharp
bil=cv.bilateralFilter(img , 10 , 25 , 25)
cv.imshow('Bilateral',bil)

cv.waitKey(0)