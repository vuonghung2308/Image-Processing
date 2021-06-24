import numpy as np
import cv2 as cv

org = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
img = np.copy(org)
kernel = np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]]
) / 16
img = cv.filter2D(img, -1, kernel)
img = cv.filter2D(img, -1, kernel)
out1 = cv.filter2D(img, -1, kernel)

out2 = img - out1

result = org + out2*1

cv.imshow('Anh goc', org)
cv.imshow('Anh mo', img)
cv.imshow('Sau 1', out2)
cv.imshow('Sau 2', result)

cv.waitKey(0)
