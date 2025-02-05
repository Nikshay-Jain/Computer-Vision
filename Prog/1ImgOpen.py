import cv2 as cv    #Add this line in Colab: from google.colab.patches import cv2_imshow()
img=cv.imread('Siberian Tiger.jpg')
cv.imshow('Big Cat',img)
print(img.shape) #gives (x,y,z) pixels. z specifies RBG layers
cv.waitKey(0)