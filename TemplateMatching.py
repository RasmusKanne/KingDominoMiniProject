import cv2 as cv
import numpy as np

# Read Image
inputPic = cv.imread("King Domino dataset/Cropped and perspective corrected boards/1.jpg")

# Converting the Image
input_gray = cv.cvtColor(inputPic, cv.COLOR_BGR2GRAY)

# Template Matching To Find Crowns
template = cv.imread("CrownTemplateResize.png", 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(input_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(inputPic, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# Showing the Result
cv.imwrite('res.png',inputPic)
cv.imshow("Correlation", res)
cv.imshow("Input Image", inputPic)
cv.waitKey(0)