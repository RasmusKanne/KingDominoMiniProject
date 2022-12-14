import cv2 as cv
import numpy as np
from Slicing import slicing
from Categorization import FindValue, Categorize
from TemplateMatching import TemplateMatching, RunNonMaxima
from GrassFire import grassfire
from CrownCounting import crown_counting
from ScoreCalculation import CalculateScore

directory = 'King Domino dataset/Cropped and perspective corrected boards'

filename = "1.jpg"

# Read Image
inputPic = cv.imread(f"{directory}/{filename}")

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

# Takes in the HSV values
# then puts them through if statements to categorize all terrain blocks into the 6 different types
c_rows = Categorize(h_rows_values, s_rows_values, v_rows_values)

# Taking all the categorized values and putting them in a 5x5 numpy array
c_image = np.array([c_rows[0],
                    c_rows[1],
                    c_rows[2],
                    c_rows[3],
                    c_rows[4]], dtype=np.uint8)

# Afterwards running a grassfire algorithm on the numpy array to find connecting blocks
grassfire(c_image)

# Finds amount of crowns using template matching
# Runs it 4 times for all 4 states of rotation the crowns are able to be in
template = cv.imread("CrownTemplateResize.png")
template_90 = cv.rotate(template, cv.ROTATE_90_CLOCKWISE)
template_180 = cv.rotate(template_90, cv.ROTATE_90_CLOCKWISE)
template_270 = cv.rotate(template_180, cv.ROTATE_90_CLOCKWISE)

templateYellow = cv.imread("CrownTemplateYellow.jpg")
templateYellow_90 = cv.rotate(templateYellow, cv.ROTATE_90_CLOCKWISE)
templateYellow_180 = cv.rotate(templateYellow_90, cv.ROTATE_90_CLOCKWISE)
templateYellow_270 = cv.rotate(templateYellow_180, cv.ROTATE_90_CLOCKWISE)

threshold = 0.55
rect1 = TemplateMatching(inputPic, template, threshold)
rect2 = TemplateMatching(inputPic, template_90, threshold)
rect3 = TemplateMatching(inputPic, template_180, threshold)
rect4 = TemplateMatching(inputPic, template_270, threshold)

yellowThreshold = 0.55
rect5 = TemplateMatching(inputPic, templateYellow, threshold)
rect6 = TemplateMatching(inputPic, templateYellow_90, threshold)
rect7 = TemplateMatching(inputPic, templateYellow_180, threshold)
rect8 = TemplateMatching(inputPic, templateYellow_270, threshold)

# Then all coordinates for crowns from the 4 template matches are put into 1 list
rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8]
all_rects = []
for i in range(len(rects)):
    for z in range(len(rects[i])):
        all_rects.append(rects[i][z])

# Then run through a non maxima supression algorithm to remove any overlapping results.
matching_result, matching_image = RunNonMaxima(inputPic, all_rects)

# Crown counting script takes the results of the template matching and matches them to the terrain blocks
# It will then return a list of rows that specifies how many crowns are on each slice
cc_rows = crown_counting(inputPic, matching_result)

# We then put the rows from crown counting and create a numpy array
cc_image = np.array([cc_rows[0],
                     cc_rows[1],
                     cc_rows[2],
                     cc_rows[3],
                     cc_rows[4]], dtype=np.uint8)

# The score is then calculated using the categorized image of ID's and the crown counting image
result = CalculateScore(c_image, cc_image)
resultImage = cv.putText(matching_image, F"Score: {result}", (175, 35), 1, 2, (0, 0, 255), 3, cv.LINE_AA)

print(f"Hue: {h_rows_values}")
print(f"Saturation: {s_rows_values}")
print(f"Value: {v_rows_values}")

print(c_rows)
print(c_image)
print(cc_image)
print(f"{filename}:{result}")

cv.imshow("template matching", resultImage)
cv.waitKey(0)