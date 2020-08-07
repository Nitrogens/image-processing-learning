import cv2
import numpy as np

img = cv2.imread("data/imori_noise.jpg")
# B, G, R = cv2.split(img)
# cv2.imwrite("data/2-B.jpg", B)
# cv2.imwrite("data/2-G.jpg", G)
# cv2.imwrite("data/2-R.jpg", R)
W, H, D = img.shape
new_W = W + 3 - W % 3
new_H = H + 3 - H % 3

max_sz = 1
img_2 = img.astype(np.float32)
img_2 = np.pad(img_2, ((max_sz, max_sz), (max_sz, max_sz), (0, 0)), 'constant', constant_values=0)

img_3 = img_2.copy()

for epoch in range(10):
    print("[Epoch] %s" % epoch)
    for i in range(max_sz, W + max_sz):
        for j in range(max_sz, H + max_sz):
            # if img_2[i, j, 0] >= 150 and img_2[i, j, 1] >= 150 and img_2[i, j, 2] >= 115:
            for k in range(3):
                # data = np.sort(img_2[(i-1):(i+2), (j-1):(j+2), k].reshape(-1))
                img_3[i, j, k] = np.min(img_2[(i-max_sz):(i+max_sz+1), (j-max_sz):(j+max_sz+1), k])
    img_2 = img_3.copy()

    img_3[img_3 > 255] = 255
    img_3[img_3 < 0] = 0

    img = img_3[max_sz:W+max_sz, max_sz:H+max_sz, :].astype(np.uint8)
    cv2.imwrite("output/10-2(%d).jpg" % epoch, img)