import cv2 as cv
import numpy as np

def CalculateScore(categorized_image, crowncount_image):
    score = 0
    for y in range(categorized_image.shape[1]):
        for x in range(crowncount_image.shape[0]):
            if crowncount_image[x, y] != 0:
                currentID = categorized_image[x, y]
                blobSize = 0
                for z in range(categorized_image.shape[0]):
                    for i in range(categorized_image.shape[1]):
                        if categorized_image[z, i] == currentID:
                            blobSize = blobSize + 1
                score = score + (blobSize * crowncount_image[x, y])

    return score