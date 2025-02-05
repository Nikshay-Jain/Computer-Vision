import cv2 as cv

def rescaleFrame(frame):
    scale=0.25
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")

img=cv.imread('Group.jpg')
img = rescaleFrame(img)
gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

faces = face_cascade.detectMultiScale(gray , 1.3 , 5)   #1.3 and 5 are randomly chosen and can be changed
print(faces)
for (x,y,w,h) in faces:
    cv.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , 3)
cv.imshow('Face',img)
cv.waitKey(0)