import cv2
import numpy as np
img=cv2.imread("photos/resim.png")
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

import cv2
import numpy as np
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img
def contrast(img):
    height, width = img.shape
    a1=.5
    a2=2
    b_img=np.zeros((height,width),np.uint8)
    w_img=np.zeros((height,width),np.uint8)
    for i in range(height):
        for j in range(width):
            b_img[i,j] = img[i,j] * a1
            w_img[i,j] = img[i,j] * a2
    cv2.imshow("b_img", b_img)
    cv2.imshow("w_img", w_img)
    cv2.waitKey(0)
img = cv2.imread("E://resim.png")
cv2.imshow("img",toGray(img))
contrast(toGray(img))

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
cv2.imshow('image 2', n_img)
cv2.waitKey(0)