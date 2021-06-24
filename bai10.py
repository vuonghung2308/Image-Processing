import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('test1.jpg', cv.IMREAD_GRAYSCALE)

out = cv.equalizeHist(img)


# plt.hist(img.ravel(), 256, [0, 256])
plt.hist(out.ravel(), 256, [0, 256])
cv.imshow('Truoc', img)
cv.imshow('Sau', out)
plt.show()

cv.waitKey(0)
