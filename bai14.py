from matplotlib import image
from matplotlib.image import imread
import numpy as np
import msvcrt as m
import cv2 as cv

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
kernel = np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]]
) / 16
img = cv.filter2D(img, -1, kernel)
img = cv.filter2D(img, -1, kernel)
out1 = cv.filter2D(img, -1, kernel)

out2 = img - out1

result = img + out2*2

cv.imshow('Anh goc', img)
cv.imshow('Sau 1', out2)
cv.imshow('Sau 2', result)

cv.waitKey(0)
