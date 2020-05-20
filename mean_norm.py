import cv2
import numpy as np
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img

img = cv2.imread("photos/cameraman.tif")
img = toGray(img)
cv2.imshow("img1",img)
m, n= img.shape 
img=img.astype(float)
n_img = np.zeros([m,n], float)

for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m-1 or j==n-1:
            n_img[i,j]=img[i,j]
            continue
        mean=img[i-1,j-1]+img[i-1,j]+img[i-1,j+1]+img[i,j-1]+img[i,j]+img[i,j+1]+img[i+1,j-1] + img[i+1,j]+img[i+1,j+1]
        mean=mean/9
        n_img[i,j]=mean
n_img = n_img.astype(np.uint8)
cv2.imshow("img",n_img)
cv2.waitKey()
