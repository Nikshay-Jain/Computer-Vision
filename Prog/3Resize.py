import cv2 as cv
def rescaleFrame(frame):    #For Photos, Videos and Live Videos
    scale=0.25
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def changeRes(width, height):   #only live video
    cap.set(3,width)
    cap.set(4,height)

img=cv.imread('Large.jpg')
cv.imshow('Large Image',img)
reimg = rescaleFrame(img)
cv.imshow('Resized',reimg)
cv.waitKey(0)

cap=cv.VideoCapture(0)  #0 - live camera else write name of video in quotes.
while True:
    isTrue,frame=cap.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('q'):    #if d is pressed or after waiting 20ms.
        break
cap.release()
cv.destroyAllWindows()