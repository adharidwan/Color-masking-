import cv2
import numpy as np


cap = cv2.VideoCapture(0)

#mask untuk warna hitam
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 30, 30])

#mask untuk warna hijau
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

#mask untuk warna biru
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

#mask untuk warna merah
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 50, 50])
upper_red2 = np.array([180, 255, 255])

while True:
    ret, frame = cap.read()
    cv2.imshow('Before',frame)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    blackmask = cv2.inRange(hsv,lower_black,upper_black)

    greenmask = cv2.inRange(hsv,lower_green,upper_green)

    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskred1 = cv2.inRange(hsv,lower_red1,upper_red1)
    maskred2 = cv2.inRange(hsv,lower_red2,upper_red2)

    maskred = cv2.bitwise_or(maskred1,maskred2)
    final_mask = cv2.bitwise_or(maskblue,maskred)

    cv2.imshow('After',maskblue)

    if cv2.waitKey(1) == ord('k'):
        break
 
cap.release()
cv2.destroyAllWindows()

