import numpy as np
import msvcrt as m
import cv2 as cv

img = cv.imread('test.jpg', cv.IMREAD_COLOR)
kernel = np.array(
    [[-1, -1, -1],
     [-1, 9, -1],
     [-1, -1, -1]])

kernel1 = np.array(
    [[1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9]])

kernel2 = np.array(
    [[0, 1, 0],
     [1, -4, 1],
     [0, 1, 0]])
     
out1 = cv.filter2D(img, -1, kernel)
out2 = cv.filter2D(img, -1, kernel1)
tmp = cv.cvtColor(out2, cv.COLOR_BGR2GRAY)
out3 = cv.filter2D(tmp, -1, kernel2)

cv.imshow('Anh goc', img)
cv.imshow('Anh sau lam net', out1)
cv.imshow('Anh sau lam min', out2)
cv.imshow('Anh sau phat hien bien', out3)

cv.waitKey(0)
