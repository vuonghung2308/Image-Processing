import cv2 as cv
import numpy as np

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)

kernel = np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]]) / 16
img = cv.filter2D(img, -1, kernel)
mx = np.array(
    [[-1, 0, 1],
     [-2, 0, 2],
     [-1, 0, 1]])

my = np.array(
    [[-1, -2, -1],
     [0, 0, 0],
     [1, 2, 1]])

out = cv.filter2D(img, -1, mx)
out1 = cv.filter2D(img, -1, my)

out2 = np.abs(out) + np.abs(out1)


t = 100

x, y = img.shape

out3 = np.copy(img)

for i in range(x):
    for j in range(y):
        if out2[i][j] > t:
            out3[i][j] = 255
        else:
            out3[i][j] = 0

cv.imshow('Truoc', img)
cv.imshow('Sau', out3)
cv.waitKey(0)
