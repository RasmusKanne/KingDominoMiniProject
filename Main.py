import cv2 as cv
import numpy as np
from Slicing import slicing

# Read Image
inputPic = cv.imread("King Domino dataset/Cropped and perspective corrected boards/1.jpg")
HSV = cv.cvtColor(inputPic, cv.COLOR_BGR2HSV)
h, s, v = cv.split(HSV)
b, g, r = cv.split(inputPic)

row1, row2, row3, row4, row5 = slicing(inputPic)

cv.imshow("h", h)
cv.imshow("s", s)
cv.imshow("v", v)

cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

cv.waitKey(0)