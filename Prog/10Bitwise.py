import cv2 as cv
import numpy as np

blank=np.zeros((400,400) , dtype='uint8')
rect = cv.rectangle(blank.copy() , (30,30) , (370,370) , 255 , -1)
circle = cv.circle(blank.copy() , (200,200) , 200 , 255, -1)
cv.imshow('Rect',rect)
cv.imshow('Circle',circle)

#Bitwise AND
bitand = cv.bitwise_and(rect,circle)
cv.imshow('Bit_AND',bitand)

#Bitwise OR
bitor = cv.bitwise_or(rect,circle)
cv.imshow('Bit_OR',bitor)

#Bitwise XOR
bitxor = cv.bitwise_xor(rect,circle)
cv.imshow('Bit_XOR',bitxor)

#Bitwise NOT
bitnot = cv.bitwise_not(circle)
cv.imshow('Rect Bit_NOT',bitnot)

cv.waitKey(0)