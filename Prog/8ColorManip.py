import cv2 as cv
import  matplotlib.pyplot as plt
import numpy as np

img=cv.imread('Raj.jpg')
cv.imshow('BGR',img)
#Interconversions allowed

#Hue-Saturation-Value
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#L*a*b - L*: Lightness , a*: Red/Green Value , b*: Blue/Yellow Value.
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#Spilting - shown as grayscale - lighter means high density of pixels of that colour
b,g,r=cv.split(img)
cv.imshow('B',b)
cv.imshow('G',g)
cv.imshow('R',r)
print(img.shape)    #shape in grayscale
print(b.shape)      #Plots Blue pixels in grayscale
print(g.shape)
print(r.shape)
merged=cv.merge([b,g,r])
cv.imshow('Merge',merged)

blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])      #Plots blue pixels
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

#Python inverts BGR colour of img after inputting so we feed RGB to get BGR
plt.imshow(rgb)
plt.show()

cv.waitKey(0)