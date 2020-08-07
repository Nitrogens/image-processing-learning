import cv2
import numpy as np

img = cv2.imread("data/imori.jpg")

# 必须通过 float32 进行计算
img_2 = img.astype(np.float32)

R = img_2[:, :, 2]
G = img_2[:, :, 1]
B = img_2[:, :, 0]
Y = 0.2126 * R + 0.7152 * G + 0.0722 * B

img_2[:, :, 0] = Y
img_2[:, :, 1] = Y
img_2[:, :, 2] = Y

# 将数据控制在 [0, 255] 范围内
img_2[img_2 > 255.0] = 255.0
img_2[img_2 < 0.0] = 0.0

img = img_2.astype(np.uint8)
cv2.imwrite("output/2-grayscale.jpg", img)


