import cv2
import numpy as np
import time
start_time = time.time()

# Load the image
img1 = cv2.imread('194.jpg')
# Convert it to greyscale
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# blur the image
blur = cv2.blur(img, (3, 3))
cv2.imshow("blur", blur)

# Threshold the image
ret, thresh = cv2.threshold(blur,50,255,0)
# Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# For each contour, find the convex hull and draw it
# on the original image.
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    cv2.drawContours(drawing, [hull], -1, (255, 255, 255), 2)
    
    

# Display the final convex hull image
cv2.imshow('ConvexHull', drawing)
cv2.imwrite('hull278.jpg', drawing)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
#cv2.imwrite('hull553.png', drawing)
cv2.waitKey(0)