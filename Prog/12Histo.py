import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Large.jpg')
cv.imshow('Large',img)
gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)
blank=np.zeros(img.shape[:2] , dtype='uint8')

#Grayscale Histogram
hist1=cv.calcHist([gray] , [0] , None , [256] , [0,256])
    #cv.calcHist([image] , [channels] , [mask(*can be None)] , [histSize] , [range of pixels])
    
#Plot
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist1)
plt.xlim([0,256])

#Masking
circle = cv.circle(blank , (gray.shape[1]//2 -50 , gray.shape[0]//2 -50) , 200 , 255 , -1)
mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('Mask',mask)

#Masked Histogram
hist2=cv.calcHist([gray] , [0] , mask , [256] , [0,256])
    #cv.calcHist([image] , [channels] , [mask(*can be None)] , [histSize] , [range of pixels])
    
#Plot
plt.figure()
plt.title('Grayscale Masked Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist2)
plt.xlim([0,256])

#hist=cv.calcHist([mask] , [0] , None , [256] , [0,256])
#after masking, major pic becomes black so histo would appear peak at 0 and rest flat but on zooming in there are small peaks too.

#Colour Histogram
colors=('b','g','r')
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])
for i,col in enumerate(colors):     #i=(0,1,2)  col=('b','g','r')
    hist3=cv.calcHist([img] , [i] , None , [256] , [0,256])
    plt.plot(hist3 , color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)