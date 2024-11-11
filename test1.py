import cv2 as cv
import sys
import math

img = cv.imread(r"C:\Users\freed\Downloads\teapot_from_utah.jpg")
if img is None:
    sys.exit("o no")
corner = img[math.floor(img.shape[0]/2):img.shape[0], math.floor(img.shape[1]/2):img.shape[1]]
print(corner.size)
print(img.size/corner.size)
img[0:math.floor(img.shape[0]/2), math.floor(img.shape[1]/2):img.shape[1]] = corner
img[math.floor(img.shape[0]/4):math.floor(img.shape[0]*3/4),math.floor(img.shape[1]/4):math.floor(img.shape[1]*3/4),2] = 0
img[math.floor(img.shape[0]/4):math.floor(img.shape[0]*3/4),math.floor(img.shape[1]/4):math.floor(img.shape[1]*3/4),1] = 0
cv.imshow("Display window",img)
k = cv.waitKey(0)