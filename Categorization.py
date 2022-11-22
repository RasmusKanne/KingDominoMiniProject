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

def Categorize(h_values, s_values, v_values):

    c_row1 = []
    c_row2 = []
    c_row3 = []
    c_row4 = []
    c_row5 = []

    c_rows = [c_row1, c_row2, c_row3, c_row4, c_row5]
    for z in range(len(h_values)):
        for i in range (len(h_values)):
            if h_values[z][i] >= 100:
                c_rows[z].append(1) # blue
            elif h_values[z][i] <= 32:
                if s_values[z][i] >= 200:
                    c_rows[z].append(2) # yellow
                elif v_values[z][i] <= 68:
                    c_rows[z].append(3) # mine
                elif v_values[z][i] <= 92:
                    c_rows[z].append(0)  # castle
                else:
                    c_rows[z].append(4) # wasteland
            else:
                if v_values[z][i] <= 75:
                    c_rows[z].append(5) # forest
                else:
                    c_rows[z].append(6) # grass

    return c_rows