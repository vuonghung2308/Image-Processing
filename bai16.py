from matplotlib.image import imread
import numpy as np
import msvcrt as m
import cv2 as cv

img = cv.imread('van.jpg', cv.IMREAD_GRAYSCALE)
kernel = cv.getStructuringElement(cv.MORPH_CROSS, (4, 4))
co = cv.morphologyEx(img, cv.MORPH_DILATE, kernel)
res = co-img
cv.imshow('Anh goc', img)
cv.imshow('Anh sau', res)

cv.waitKey(0)