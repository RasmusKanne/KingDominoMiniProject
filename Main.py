import cv2 as cv
import numpy as np

inputPic = cv.imread("1.jpg")

input_gray = cv.cvtColor(inputPic, cv.COLOR_BGR2GRAY)
template = cv.imread("CrownTemplate.png", 0)

res = cv.matchTemplate(input_gray,template,cv.TM_CCORR_NORMED)

cv.imshow("Correlation", res)
cv.imshow("Input Image", inputPic)
cv.waitKey(0)