import cv2
import numpy as np
import toGray as g

img=cv2.imread("photos/resim.png")
cv2.imshow('image11', img)
img=g.toGray(img)
height, width = img.shape
n_img=np.zeros((height,width),np.uint8)

for i in range(height):
    for j in range(width):
        if i==0 or j==0 or i == height-1 or j == width-1:
            n_img[i,j] = img[i,j]
            continue
        top=img[i-1,j-1]*1+img[i-1,j]*2+img[i-1,j+1]*1+img[i,j-1]*2+img[i,j]*4+img[i,j+1]*2+img[i+1,j-1]*1 + img[i+1,j]*2+img[i+1,j+1]*1
        n_img[i,j]=top/16
cv2.imshow('image1', img)
cv2.imshow('image2', n_img)
cv2.waitKey(0)