import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
out = np.copy(img)
x, y = img.shape

for i in range(x):
    for j in range(y):
        out[i][j] = 20*np.log(1+img[i][j])

# print(img)

# plt.hist(img.ravel(), 256, [0, 256])
plt.hist(out.ravel(), 256, [0, 256])
cv.imshow('Truoc', img)
cv.imshow('Sau', out)
plt.show()

cv.waitKey(0)
