import cv2 as cv
import numpy as np

def FindValue(inputRows):

    fv_row1 = []
    fv_row2 = []
    fv_row3 = []
    fv_row4 = []
    fv_row5 = []

    fv_rows = [fv_row1, fv_row2, fv_row3, fv_row4, fv_row5]
    for z in range(len(fv_rows)):
        for i in range(len(fv_rows)):
            fv_rows[z].append(np.median(inputRows[z][i]))

    return fv_rows