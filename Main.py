import cv2 as cv
import numpy as np
from Slicing import slicing

# Read Image
inputPic = cv.imread("1.jpg")

row1, row2, row3, row4, row5 = slicing(inputPic)

cv.imshow("1", row3[4])
cv.waitKey(0)