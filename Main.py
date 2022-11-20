import cv2 as cv
import numpy as np
from Slicing import slicing
from Categorization import FindValue, Categorize

# Read Image
inputPic = cv.imread("King Domino dataset/Cropped and perspective corrected boards/10.jpg")

# Convert and split HSV channels
HSV = cv.cvtColor(inputPic, cv.COLOR_BGR2HSV)
h, s, v = cv.split(HSV)

# slicing() takes an image and returns five lists consisting of five sliced images in a 5x5 grid
# Slicing the hue channel
h_rows = slicing(h)

# Slicing the saturation channel
s_rows = slicing(s)

# Slicing the value channel
v_rows = slicing(v)

# FindValue() finds the median value of each image in the sliced image lists
# Then puts them in a new list and returns them
h_rows_values = FindValue(h_rows)
s_rows_values = FindValue(s_rows)
v_rows_values = FindValue(v_rows)

# Takes in the HSV values and puts them through if statements to categorize all terrain blocks into the 6 different types
c_rows = Categorize(h_rows_values, s_rows_values, v_rows_values)

print(f"Hue: {h_rows_values}")
print(f"Saturation: {s_rows_values}")
print(f"Value: {v_rows_values}")

print(c_rows)

cv.imshow("Input", inputPic)
cv.waitKey(0)