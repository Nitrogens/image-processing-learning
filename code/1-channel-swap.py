import cv2
import numpy

img = cv2.imread("data/imori.jpg")
red = img[:, :, 2].copy()
green = img[:, :, 1].copy()
blue = img[:, :, 0].copy()
img[:, :, 0] = red
img[:, :, 2] = blue
cv2.imshow("", img)
cv2.waitKey(0)
cv2.imwrite("output/1-channel-swap.jpg", img)
