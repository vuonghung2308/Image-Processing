import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('test1.jpg', cv.IMREAD_GRAYSCALE)

out = cv.equalizeHist(img)

fig, axs = plt.subplots(2)
axs[0].hist(img.ravel(), 256, [0, 256])
axs[0].set_title("Ảnh gốc")
axs[1].hist(out.ravel(), 256, [0, 256])
axs[1].set_title("Ảnh sau cân bằng xám")
cv.imshow('Truoc', img)
cv.imshow('Sau', out)

plt.show()

cv.waitKey(0)