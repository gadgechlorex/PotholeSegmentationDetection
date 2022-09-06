import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import time
start_time = time.time()

img = cv.imread('278.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(gray)
cv.imshow('input1', img)
ret, thresh = cv.threshold(dst,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# noise removal
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.3*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv.connectedComponents(sure_bg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv.watershed(img,markers)
img[markers == -1] = [0,255,0]

cv.imshow('input', img)
#cv.imshow('gray',gray)
cv.imshow('opening', opening)
cv.imwrite('timing.jpg', opening)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
cv.waitKey(0)
