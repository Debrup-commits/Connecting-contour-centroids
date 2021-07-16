import numpy as np
import cv2

img = cv2.imread('image.PNG')

#converting to BnW
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#thresholding
ret, thresh = cv2.threshold(img_gray, 240, 255, 0)

#finding and printing no.of contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(f"NUmber of contours = {str(len(contours))}")

#drawing contours
cv2.drawContours(img, contours, -1, (255, 255, 255), 1)

#function to identify centroids
def identify_centroid(image, centroid):
    cent_moment = cv2.moments(centroid)
    centroid_x = int(cent_moment['m10']/cent_moment['m00'])
    centroid_y = int(cent_moment['m01']/cent_moment['m00'])
    
    return image

#identifying the centroids
for (i, c) in enumerate(contours):
    orig = identify_centroid(img, c)

#drawing lines    
img = cv2.line(img, (141, 131), (516, 551), (0, 0, 0), 1)
img = cv2.line(img, (516, 551), (666, 355), (0, 0, 0), 1)
img = cv2.line(img, (666, 355), (909, 257), (0, 0, 0), 1)
img = cv2.line(img, (909, 257), (366, 295), (0, 0, 0), 1)
img = cv2.line(img, (366, 295), (161, 571), (0, 0, 0), 1)
img = cv2.line(img, (161, 571), (674, 138), (0, 0, 0), 1)
img = cv2.line(img, (674, 138), (909, 537), (0, 0, 0), 1)

cv2.imshow('Image', img)
#cv2.imshow('BnW', img_gray)
#cv2.imshow('thresholded', thresh)

#Saving output
cv2.imwrite('Output.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows
