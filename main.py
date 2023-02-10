# This is a sample Python script.
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


def threshold(img, thresh):
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            if img[y, x] > thresh:
                img[y, x] = 255
            else:
                img[y, x] = 0
    return img

def findT(hist):
    max =0
    max_index = -1
    for i in range(hist.shape[0]):
        if hist[i] > max:
            max = hist[i]
            max_index = i
    return max_index - 50



i = 1
while True:
    img = cv.imread(r'Orings\Oring'+str(i)+'.jpg', 0)
    i = i + 1
    if i==16:
        i=1
    hist = imhist(img)
    thresh = findT(hist)
    bw = threshold(img.copy(), thresh)
    plt.plot(hist)
    img = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    cv.putText(img,'FAIL', (20,20),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
    cv.circle(img,(50,50),20,(0,255,0))
    cv.imshow('binary', bw)
    cv.imshow('oring', img)
    plt.show()
    c = cv.waitKey()
    if c & 0xFF == ord('q'):
        break
