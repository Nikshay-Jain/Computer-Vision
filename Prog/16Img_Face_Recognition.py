import cv2 as cv
import numpy as np
import face_recognition

def rescaleFrame(frame):
    scale = 0.7
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

face1=face_recognition.load_image_file('elon.jpg')
face1_encoding=face_recognition.face_encodings(face1)[0]

face2=face_recognition.load_image_file('Donald Trump.jpg')
face2_encoding=face_recognition.face_encodings(face2)[0]

face3=face_recognition.load_image_file('Prash1.jpg')
face3_encoding=face_recognition.face_encodings(face3)[0]

face4=face_recognition.load_image_file('Large.jpg')
face4_encoding=face_recognition.face_encodings(face4)[0]

known=[face1_encoding,
       face2_encoding,
       face3_encoding,
       face4_encoding]

known_names=["Elon Musk",
             "Donald Trump",
             "Prashant Jain",
             "Nikshay Jain"]

file_name = "Nik (1).jpg"
unknown_image = rescaleFrame(cv.imread(file_name))
unknown_draw = rescaleFrame(cv.imread(file_name))

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image,face_locations)

for (top,right,bottom,left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known , face_encoding)
    name = "Unknown"

    face_distances = face_recognition.face_distance(known , face_encoding)
    best_match_index = np.argmin(face_distances)

    if matches[best_match_index]:
        name = known_names[best_match_index]
        cv.rectangle(unknown_draw , (left,top) , (right,bottom) , (0,255,0) , 3)
        cv.putText(unknown_draw , name , (left,top-20) , cv.FONT_HERSHEY_SIMPLEX , 1 , (0,255,0) , 2 , cv.LINE_AA)

cv.imshow('Detected',unknown_draw)
cv.waitKey(0)