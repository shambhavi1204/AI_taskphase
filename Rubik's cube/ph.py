import cv2
import numpy as np
from imutils import contours

image = cv2.imread('images.jpeg')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = np.zeros(image.shape, dtype=np.uint8)

colors = {
    'gray': ([76, 0, 41], [179, 255, 70]),        
    'blue': ([69, 120, 100], [179, 255, 255]),    
    'yellow': ([21, 110, 117], [45, 255, 255]),   
    'orange': ([0, 110, 125], [17, 255, 255]),  
    'white' : ([0, 0, 255], [255, 255, 255]),
    'green' : ([45, 100, 100], [75, 255, 255])
    }

# Color threshold to find the squares
open_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)) #a rectangle kernal of(7,7)
close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) # a rectangle kernal of (5,5)

for color, (lower, upper) in colors.items():
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    color_mask = cv2.inRange(image, lower, upper)
    color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, open_kernel, iterations=1) #erosion followed by dilation
    color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_CLOSE, close_kernel, iterations=5)
#dilation followed by Erosion
    color_mask = cv2.merge([color_mask, color_mask, color_mask])
    mask = cv2.bitwise_or(mask, color_mask)
#masking the desired region
gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
(cnts, _) = contours.sort_contours(cnts, method="top-to-bottom")

# Take each row of 3 and sort from left-to-right or right-to-left
cube_rows = []
row = []
for (i, c) in enumerate(cnts, 1):
    row.append(c)
    if i % 3 == 0:  
        (cnts, _) = contours.sort_contours(row, method="left-to-right") #sorting the contours fron left to right in the list cents
        cube_rows.append(cnts)
        row = []

# Draw text
number = 0
for row in cube_rows:
    for c in row:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(original, (x, y), (x + w, y + h), (36,255,12), 2)

        cv2.putText(original, "#{}".format(number + 1), (x,y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        number += 1

cv2.imshow('mask', mask)
cv2.imwrite('mask.jpg', mask)
cv2.imshow('original', original)
cv2.waitKey()
