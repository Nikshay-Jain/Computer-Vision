import cv2 as cv
import numpy as np

#Resize                 x-->Right   y-->Down    -ve accordingly
img=cv.imread('4K.jpg')
w=img.shape[1]//4
h=img.shape[0]//4
d=(w,h)
img=cv.resize(img, d, interpolation=cv.INTER_AREA)
cv.imshow('4K',img)

#Translation
def trans(img,x,y):
    trMat=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,trMat,dim)

tr=trans(img,100,-100)
cv.imshow('Translated',tr)

#Rotation
def rot(img,ang,rotPoint=None):
    (ht,wd)=img.shape[:2]
    if rotPoint is None:
        rotPoint = (wd//2,ht//2)    #Sets centre of rotation to midpt
    rotMat=cv.getRotationMatrix2D(rotPoint,ang,1.0)
    dim=(wd,ht)
    return cv.warpAffine(img,rotMat,dim)

rt=rot(img,30)
cv.imshow('Rotated',rt)

#Flip       0 - Origin, 1 - Y axis, -1 - X axis
flip=cv.flip(img,0)
cv.imshow('Flip',flip)

#Resize
res=cv.resize(img , (150,150) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',res)

#Crop
crop=img[50:200, 50:150]
cv.imshow('Croped',crop)

cv.waitKey(0)