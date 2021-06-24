from sklearn.cluster import KMeans
import cv2 as cv
import numpy as np

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
x, y = img.shape
res = np.copy(img)
res = res.reshape(x*y, 1)

kmeans = KMeans(2).fit(res)
label = kmeans.predict(res)

value1 = kmeans.cluster_centers_[0]
value2 = kmeans.cluster_centers_[1]

delta1 = 255 - value1
delta2 = 255 - value1
if delta1 > delta2:
    value1 = 0
    value2 = 255
else:
    value2 = 0
    value1 = 255

kmeans.cluster_centers_[0] = value1
kmeans.cluster_centers_[1] = value2
for k in range(2):
    res[label == k] = kmeans.cluster_centers_[k]

for i in range(x*y):
    tmp = 255 - res[i]

res = res.reshape(x, y)
cv.imshow('Anh Goc', img)
cv.imshow('Anh Phan Nguong KMean', res)
cv.waitKey(0)
