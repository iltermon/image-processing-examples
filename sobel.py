import cv2
import numpy as np
img=cv2.imread("photos/rice.jpg")
cv2.imshow('image', img)
cv2.waitKey(0)
gx=[[-1,0,1],[-2,0,2],[-1,0,1]]
gy=[[1,2,1],[0,0,0],[-1,-2,-1]]
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img

img=toGray(img)

x,y = img.shape
n_img=np.zeros((x+2,y+2),np.uint8)
G=np.zeros((x,y))
n_img[1:x+1,1:y+1] = img
img = img.astype(float)
for i in range(x):
    for j in range(y):
        bir = np.multiply(n_img[i:i+3,j:j+3],gx)
        iki = np.multiply(n_img[i:i+3,j:j+3],gy)
        birtoplam=sum(sum(bir))
        ikitoplam=sum(sum(iki))
        G[i,j] = abs(birtoplam) + abs(ikitoplam)
        if G[i,j]<100:
            G[i,j]=np.uint8(0)
        else:
            G[i,j]=np.uint8(255)
G=G.astype(np.uint8)
print(G)
cv2.imshow('image', G)
cv2.waitKey(0)
