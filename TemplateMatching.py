import cv2 as cv
import numpy as np
from NonMaximaSupression import non_max_suppression

# Read Image
# inputPic = cv.imread("King Domino dataset/Cropped and perspective corrected boards/1.jpg")

# Converting the Image
# input_gray = cv.cvtColor(inputPic, cv.COLOR_BGR2GRAY)

# Template Matching To Find Crowns
# template = cv.imread("CrownTemplateResize.png", 0)

def TemplateMatching(processed, template, thresholdValue):
    #image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    processed = np.array(processed, dtype=np.uint8)
    template = np.array(template, dtype=np.uint8)
    tH, tW = template.shape[:2]

    res = cv.matchTemplate(processed, template, cv.TM_CCOEFF_NORMED)
    threshold = thresholdValue
    (yCoords, xCoords) = np.where(res >= threshold)

    rects = []
    for (x, y) in zip(xCoords, yCoords):
        rects.append((x, y, x + tW, y + tH))

    # show the output image
    return rects

def RunNonMaxima(image, rects):
    result = image.copy()
    pick = non_max_suppression(np.array(rects), 0.1)
    # resultAmount = len(pick)
    # print(resultAmount)

    # loop over the final bounding boxes
    for (startX, startY, endX, endY) in pick:
        # draw the bounding box on the image
        cv.rectangle(result, (startX, startY), (endX, endY),
                      (0, 0, 255), 3)
    return pick, result

# Showing the Result
# cv.imwrite('res.png',inputPic)
# cv.imshow("Correlation", res)
# cv.imshow("Input Image", inputPic)
# cv.waitKey(0)