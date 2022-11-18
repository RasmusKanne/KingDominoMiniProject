import cv2 as cv
import numpy as np

# input = cv.imread("1.jpg")

def slicing(image):
    oriImage = image.copy()

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []

    rows = [row1, row2, row3, row4, row5]

    for z in range(5):
        for i in range(5):
            x_start = i * image.shape[1]//5
            y_start = z * image.shape[0]//5
            x_end = (i + 1) * image.shape[1]//5
            y_end = (z + 1) * image.shape[0]//5
            refPoint = [(x_start, y_start), (x_end, y_end)]
            slice = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            rows[z].append(slice)

    return rows

#row1, row2, row3, row4, row5 = slicing(input)