"""
Now let's try with `cv2.CHAIN_APPROX_SIMPLE`

method applied:
1. grayscale
2. bilateral filter ( remove noise)
3. otsu binary thresholding
4. contours
5. hull convex
6. draw contours & hull

"""
import time
import cv2 
import numpy as np
from matplotlib import pyplot as plt
start_time = time.time()

image = cv2.imread('278.jpg') #553


# convert image to gray scale
src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# dst = cv2.equalizeHist(src)
ret, thresh = cv2.threshold(src,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)

# detect the contours on the binary image using cv2.ChAIN_APPROX_SIMPLE
contours1, hierarchy1 = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw contours on the original image for `CHAIN_APPROX_SIMPLE`
image_copy1 = image.copy()
cv2.drawContours(image_copy1, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results


cv2.imshow('gray',thresh)

cv2.imshow('Simple approximation', image_copy1)
cv2.imwrite('timing.jpg', opening)
cv2.imshow("output",opening)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
cv2.waitKey(0)
plt.show()
