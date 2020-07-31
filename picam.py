import os, errno
import cv2
import numpy as np
from time import sleep
from datetime import datetime

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

cv2.namedWindow("PiCam")

img_counter = 0
scale = 50
dim = (648,486)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (5,20)
fontScale              = 0.4
fontColor              = (255,255,255)
lineType               = 1

# create the images folder if doesn't exist
try:
    os.makedirs('images')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    now = datetime.now()
    resized = cv2.resize(frame,dim)
    cv2.putText(resized, now.strftime('%c%Z'), bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    cv2.imshow("PiCam", resized)
    #cv2.imshow("PiCam", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        cam.release()
        cv2.destroyAllWindows()
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "PiCam_{}.png".format(now.strftime('%Y%m%d%H%M%S'))
        cv2.imwrite('images/' + img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

#cam.release()
#cv2.destroyAllWindows()
