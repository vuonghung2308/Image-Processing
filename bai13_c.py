from matplotlib.image import imread
import numpy as np
import msvcrt as m
import cv2 as cv

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
lap = np.array(
    [[0, 1, 0],
     [1, -4, 1],
     [0, 1, 0]]
)
kernel1 = np.array(
    [[1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9]]
)
out2 = cv.filter2D(img, -1, kernel1)
out3 = cv.filter2D(out2, -1, lap)

out4 = img + out3

cv.imshow('Anh goc', img)
cv.imshow('Anh sau lam min', out3)
cv.imshow('Anh sau phat hien bien', out4)

cv.waitKey(0)
