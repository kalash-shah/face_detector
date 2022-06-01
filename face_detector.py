import cv2
from random import randrange
# loading some pre=trained data face frontals from opencv. (haarcascade alg)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# importing image 
#RDJ_image = cv2.imread('RDJ2.jpg')
#bill_and_steve = cv2.imread('steve_jobs_and_bill_gates.jfif')
my_webcam = cv2.VideoCapture(0)
while True:
    # reading a particular frame of the video. 
    successful_frame, frame = my_webcam.read()
    """
     .read() method provides you with two value. First whether it can capture the image. 
     (bolean value) and second will be the actual image or frame.
    """
    # converting image to grayscale cause out alg. can only understand greyscale images. It is lot easier to do it.
    greyscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(greyscale_image)
    for (x,y,w,h) in face_coordinates:

        """
        This above command will give identify the face and give you the co-ordinates of the face.
        but it will give you in a different way. what this will do is this will give you the top 
        left co-ordinate and the width and the height of the rectangle. 
        randrange(256), randrange(256), randrange(256)
        """
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 3)
    """
    Here .rectangle takes arguments as follows:-
    1) image
    2) top left co-ordinate
    3) bottom right co-ordinate
    4) color of the reactanglewow
    5) width
    """
    cv2.imshow('Me!!', frame)
    key = cv2.waitKey(1)
    # ASCII value of Q and q
    if key==81 or key==113:
        break
 