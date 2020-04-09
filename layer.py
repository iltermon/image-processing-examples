import cv2
import numpy as np
img=cv2.imread("E://resim.png")
cv2.imshow('image', img)


R=img[:,:,0]
G=img[:,:,1]
B=img[:,:,2]
cv2.imshow("R",R)

cv2.imshow("G",G)

cv2.imshow("B",B)
n_img = np.zeros((477,686,3), np.uint8)
n_img[:,:,0]=R
n_img[:,:,1]=G
n_img[:,:,2] = B
cv2.imshow("n_img",n_img)
cv2.waitKey(0)