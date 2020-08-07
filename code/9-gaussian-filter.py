import cv2
import numpy as np

img = cv2.imread("data/imori_noise.jpg")
W, H, D = img.shape
new_W = W + 3 - W % 3
new_H = H + 3 - H % 3

img_2 = img.astype(np.float32)
img_2 = np.pad(img_2, ((1, 1), (1, 1), (0, 0)), 'constant', constant_values=0)

M = np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]], dtype=np.float32)
M /= 16.0
print(M)

img_3 = img_2.copy()
for i in range(1, W + 1):
    for j in range(1, H + 1):
        for k in range(3):
            img_3[i, j, k] = np.sum(img_2[(i-1):(i+2), (j-1):(j+2), k] * M)

img_3[img_3 > 255] = 255
img_3[img_3 < 0] = 0

img_3 = img_3[1:W+1, 1:H+1, :]

img = img_3.astype(np.uint8)
cv2.imwrite("output/9-1.jpg", img)