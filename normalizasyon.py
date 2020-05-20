import cv2
import numpy as np
def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img

img = cv2.imread("photos\\resim.png")
cv2.imshow("img",img)
cv2.imshow("img_g",toGray(img))
n_img=toGray(img)
n_max=50
n_min=10
height, width = n_img.shape
n_img = n_img.astype(float)
_min=float(np.amin(n_img))
_max=float(np.amax(n_img))
print(_max)
for i in range(height):
    for j in range(width):
        I = n_img[i,j]
        Inew=(I-_min)*((n_max-n_min))/(_max-_min)+n_min
        n_img[i,j] = Inew
n_img = n_img.astype(np.uint8)
cv2.imshow("img1",n_img)
cv2.waitKey(0)