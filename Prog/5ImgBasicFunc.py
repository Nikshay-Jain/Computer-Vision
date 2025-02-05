import cv2 as cv

#Original
img=cv.imread('Tiger.jpg')
cv.imshow('Color',img)

#Grayscale
gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#Blur
blur=cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #Tuple in () indcate level of blurness
cv.imshow('Blur',blur)

#Edge Casscade
canny=cv.Canny(blur, 125 , 175)
cv.imshow('Casscade',canny)

#Dilate
dia=cv.dilate(canny , (7,7) , iterations=3)
cv.imshow('Dilate',dia)

#Erode
ero=cv.erode(dia , (7,7) , iterations=3)    #Gives us casscade back from dilated so opposite.
cv.imshow('Eroded',ero)

#Binarising ie Thresholding ie each pixel above 125 is black rest white only
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)



cv.waitKey(0)