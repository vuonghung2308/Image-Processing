import cv2 as cv
import numpy as np

img = cv.imread('test.jpg', cv.IMREAD_COLOR)

kernel = np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]]) / 16

out = cv.filter2D(img, -1, kernel)
cv.imshow('Truoc', img)
cv.imshow('Sau', out)
cv.waitKey(0)
