import cv2
import numpy as np
import time
from collections import deque

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("HH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("HS", "Tracking", 255, 255, nothing)
cv2.createTrackbar("HV", "Tracking", 255, 255, nothing)

pts = deque(maxlen=20)

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
time.sleep(3)

for i in range(30):
    check,img=video.read()
    

while(video.isOpened()):
    check,frame = video.read()
    if check==False:
        break
    
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_h = cv2.getTrackbarPos("LH", "Tracking")
    lower_s = cv2.getTrackbarPos("LS", "Tracking")
    lower_v = cv2.getTrackbarPos("LV", "Tracking")

    upper_h = cv2.getTrackbarPos("HH", "Tracking")
    upper_s = cv2.getTrackbarPos("HS", "Tracking")
    upper_v = cv2.getTrackbarPos("HV", "Tracking")

    lower_shade = np.array([lower_h, lower_s, lower_v])
    upper_shade = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_shade, upper_shade)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2) 

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
        
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    pts.appendleft(center)

    for i in range(1, len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue
        
	
            
        thickness = int(np.sqrt(20 / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

	
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

	
    if key == ord("q"):
        break
            

cap.release()
cv2.destroyAllWindows()  
        
