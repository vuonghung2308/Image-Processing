import numpy as np
import cv2 as cv
import random


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = np.copy(data)
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
noise = sp_noise(img, 0.05)
removed_noise = median_filter(noise, 4)
cv.imshow("Truoc", img)
cv.imshow("Nhieu", noise)
cv.imshow('Sau', removed_noise)

cv.waitKey(0)
