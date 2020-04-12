import cv2
import numpy as np
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img
def lightning(img):
    height, width = img.shape
    b1=-50
    b2=50
    b_img=np.zeros((height,width),np.uint8)
    w_img=np.zeros((height,width),np.uint8)
    for i in range(height):
        for j in range(width):
            b_img[i,j] = img[i,j] + b1
            w_img[i,j] = img[i,j] + b2
    cv2.imshow("b_img", b_img)
    cv2.imshow("w_img", w_img)
    cv2.waitKey(0)
img = cv2.imread("E://resim.png")
cv2.imshow("img",toGray(img))
lightning(toGray(img))
