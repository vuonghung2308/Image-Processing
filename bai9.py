import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
out = np.copy(img)
x, y = img.shape

t = 127

for i in range(x):
    for j in range(y):
        if img[i][j] > t:
            out[i][j] = 255
        else:
            out[i][j] = 0

# plt.hist(img.ravel(), 256, [0, 256])
plt.hist(out.ravel(), 256, [0, 256])
cv.imshow('Truoc', img)
cv.imshow('Sau', out)
plt.show()

cv.waitKey(0)
