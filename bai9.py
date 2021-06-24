import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)

x, y = img.shape

t1 = 80
out1 = np.copy(img)

for i in range(x):
    for j in range(y):
        if img[i][j] > t1:
            out1[i][j] = 255
        else:
            out1[i][j] = 0

t2 = 100
out2 = np.copy(img)

for i in range(x):
    for j in range(y):
        if img[i][j] > t2:
            out2[i][j] = 255
        else:
            out2[i][j] = 0


t3 = 120
out3 = np.copy(img)

for i in range(x):
    for j in range(y):
        if img[i][j] > t3:
            out3[i][j] = 255
        else:
            out3[i][j] = 0



t4 = 140
out4 = np.copy(img)

for i in range(x):
    for j in range(y):
        if img[i][j] > t4:
            out4[i][j] = 255
        else:
            out4[i][j] = 0

cv.imshow('Truoc', img)
cv.imshow('Sau 1', out1)
cv.imshow('Sau 2', out2)
cv.imshow('Sau 3', out3)
cv.imshow('Sau 4', out4)

plt.show()
cv.waitKey(0)