import cv2 as cv
import numpy as np
from Slicing import slicing
from Categorization import FindValue

# Read Image
inputPic = cv.imread("King Domino dataset/Cropped and perspective corrected boards/1.jpg")

# Convert and split HSV channels
HSV = cv.cvtColor(inputPic, cv.COLOR_BGR2HSV)
h, s, v = cv.split(HSV)

# Slicing the hue channel
h_rows = slicing(h)

# Slicing the saturation channel
s_rows = slicing(s)

# Slicing the value channel
v_rows = slicing(v)

# Categorizing by finding the median values in each channel
h_rows_values = FindValue(h_rows)
s_rows_values = FindValue(s_rows)
v_rows_values = FindValue(v_rows)

print(h_rows_values)
print(s_rows_values)
print(v_rows_values)
cv.waitKey(0)