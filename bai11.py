from matplotlib.image import imread
import numpy as np
import cv2 as cv

img = cv.imread('noise.jpg', cv.IMREAD_COLOR)
kernel1 = np.array(
    [[1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9]])

kernel = np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]]) / 16

out = cv.filter2D(img, -1, kernel1)
out1 = cv.filter2D(img, -1, kernel)

cv.imshow('Anh goc', img)
cv.imshow('Sau 1', out)
cv.imshow('Sau 2', out1)

cv.waitKey(0)
