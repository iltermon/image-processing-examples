import cv2
import numpy as np
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img
def cut(img,x,y):
    n_img=np.zeros((90,90),np.uint8)
    for i in range(90):
        for j in range(90):
            n_img[i,j]=img[x+i,y+j]
    return n_img

x=int(input('SATIR: '))
y=int(input('SUTUN: '))

img = cv2.imread("E://resim.png")
cv2.imshow("img",img)
cv2.imshow("img",toGray(img))
cv2.imshow("n_img_binary", cut(toGray(img),x,y))
cv2.waitKey(0)