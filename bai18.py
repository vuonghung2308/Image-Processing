from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('test.jpg', 0)
t, res = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
print(t)

cv.imshow('truoc', img)
cv.imshow('Sau', res)
plt.hist(res.ravel(), 256, [0, 256])
plt.show()
cv.waitKey(0)
