import cv2
import numpy as np

img = cv2.imread("data/imori.jpg")
W, H, D = img.shape

img_2 = img.astype(np.float32)

for i in range(0, W, 8):
    for j in range(0, H, 8):
        for k in range(3):
            avg_value = np.max(img_2[i:i+8, j:j+8, k])
            img_2[i:(i + 8), j:(j + 8), k] = avg_value

img_2[img_2 > 255] = 255
img_2[img_2 < 0] = 0

img = img_2.astype(np.uint8)
cv2.imwrite("output/8-max-pooling.jpg", img)