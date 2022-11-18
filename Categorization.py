import cv2 as cv
import numpy as np

def FindValue(row):

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []

    rows = [row1, row2, row3, row4, row5]
    for z in range(len(rows)):
        for i in range(len(rows)):
            rows[z].append(np.median(row[i]))

    return rows