import cv2 as cv

img = cv.imread('van.jpg', cv.IMREAD_GRAYSCALE)
kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
co = cv.morphologyEx(img, cv.MORPH_DILATE, kernel)
da = cv.morphologyEx(co, cv.MORPH_ERODE, kernel)
da = cv.morphologyEx(da, cv.MORPH_ERODE, kernel)
co = cv.morphologyEx(da, cv.MORPH_ERODE, kernel)

cv.imshow('Anh goc', img)
cv.imshow('Anh sau', co)

cv.waitKey(0)
