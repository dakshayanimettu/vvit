#face recognition:storing images
import cv2, sys, numpy, os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  
print('Enter the name of the label')
sub_data=input()  
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.makedirs(path,exist_ok=True)
# defining the size of images  
(width, height) = (130, 100)    
#'0' is used for my webcam,  
# if you've any other camera
#  attach use '1' like this
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)  
# The program loops until it has 100 images of the face.
count = 1
while count < 100 and webcam.isOpened():  
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
    count += 1
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()

