# This is a sample Python script.
import queue

import cv2 as cv
import numpy as np
import time
import timeit
import matplotlib.pyplot as plt


def imhist(img):
    hist = np.zeros(256)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            hist[img[x, y]] += 1
    return hist

def erosion(img):
    temp = img.copy()
    for y in range(1, img.shape[0] -1):
        for x in range(1, img.shape[1] -1):
            target = img[y, x]
            up = img[y - 1, x]
            down = img[y + 1, x]
            left = img[y, x - 1]
            right = img[y, x + 1]

            if target == 255 and (up == 0 or down == 0 or left == 0 or right == 0):
                temp[y, x] = 0

    return temp

def dilation(img):
    temp = img.copy()
    for y in range(1, img.shape[0] - 1):
        for x in range(1, img.shape[1] - 1):
            target = img[y, x]
            up = img[y - 1, x]
            down = img[y + 1, x]
            left = img[y, x - 1]
            right = img[y, x + 1]

            if target == 0 and (up == 255 or down == 255 or left == 255 or right == 255):
                temp[y, x] = 255

    return temp

def ccl(img):
    temp = img.copy()
    queue = []
    curlab = 1
    # for y in range(1, img.shape[0] - 1):
    #     for x in range(1, img.shape[1] - 1):
    #         if img[y,x] is not labeled:
    #             img[y,x] = curlab


def threshold(img, thresh):
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            if img[y, x] > thresh:
                img[y, x] = 0
            else:
                img[y, x] = 255
    return img

#find the threshold value using the histogram
def findT(hist):
    max =0
    max_index = -1
    for i in range(hist.shape[0]):
        if hist[i] > max:
            max = hist[i]
            max_index = i
    return max_index - 50





#i = variable to access the images
i = 1
while True:
    img = cv.imread(r'Orings\Oring'+str(i)+'.jpg', 0)
    i = i + 1
    #when the last image is reached, start from the first image
    if i==16:
        i=1

    #get the histogram of the image
    hist = imhist(img)

    #get the threshold value
    thresh = findT(hist)

    #threshold the image using the threshold value
    bw = threshold(img.copy(), thresh)

    #plot the histogram
    plt.plot(hist)
    img = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    cv.putText(img,'FAIL', (20,20),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
    cv.circle(img,(50,50),20,(0,255,0))
    cv.imshow('binary', bw)
    cv.imshow('oring', img)
    cv.imshow('dilate-erode', erosion(dilation(bw)))
    plt.show()
    c = cv.waitKey()
    if c & 0xFF == ord('q'):
        break
