import cv2
import numpy as np

img = cv2.imread("data/imori.jpg")  # Read image
# cv2.imshow("imori", img)          # Show image
# cv2.waitKey(0)                    # Wait for any input
# cv2.destroyAllWindows()           # Close the window
print(img.shape)                    # Size
print(img.dtype)

# _img = img.astype(np.float32)

print(img[20, 30])      # BGR
print(img[20, 30, 1])

print(img[20, 30:33])
img2 = img.copy()
img2[:50, :50] = 0
# cv2.imshow("", img2); cv2.waitKey(0)

cv2.imwrite("output/0-tutorial.jpg", img2)