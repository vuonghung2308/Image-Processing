from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('test.jpg', 0)
t, res = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
print(t)

cv.imshow('truoc', img)
cv.imshow('Sau', res)

fig, axs = plt.subplots(2)
axs[0].hist(img.ravel(), 256, [0, 256])
axs[0].set_title("Ảnh gốc")
axs[1].hist(res.ravel(), 256, [0, 256])
axs[1].set_title("Ảnh sau phân ngưỡng")
plt.show()
cv.waitKey(0)
