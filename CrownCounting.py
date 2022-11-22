import cv2 as cv
import numpy as np

# input = cv.imread("1.jpg")

def crown_counting(image, crownCoords):

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []

    rows = [row1, row2, row3, row4, row5]

    for z in range(5):
        for i in range(5):
            currentCrownCount = 0
            for j in range(len(crownCoords)):
                x_start = i * image.shape[1]//5
                y_start = z * image.shape[0]//5
                x_end = (i + 1) * image.shape[1]//5
                y_end = (z + 1) * image.shape[0]//5
                refPoint = [(x_start-5, y_start-5), (x_end+5, y_end+5)]
                crownPoint = [(crownCoords[j][0], crownCoords[j][1]), (crownCoords[j][2], crownCoords[j][3])]
                if refPoint[0][1] <= crownPoint[0][1] and refPoint[0][0] <= crownPoint[0][0] and refPoint[1][1] >= crownPoint[1][1] and refPoint[1][0] >= crownPoint[1][0]:
                    currentCrownCount = currentCrownCount + 1
            rows[z].append(currentCrownCount)

    return rows