import cv2
import numpy as np
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img

def rotate(img):
    width, height = img.shape
    transpose_img = np.transpose(img)
    n_img=np.zeros((height,width), np.uint8)
    for i in range(height):
        for j in range(width):
            n_img[i,j]=transpose_img[i,width-j-1]
    return n_img
img = cv2.imread("E://resim.png")
cv2.imshow("img",toGray(img))
cv2.imshow("n_img",rotate(toGray(img)))
cv2.waitKey(0)

