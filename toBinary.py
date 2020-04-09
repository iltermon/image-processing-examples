import cv2
import numpy as np

def toGray(img):
    height, width, channels = img.shape
    n_img=np.zeros((height,width),np.uint8)

    for i in range(height):
        for j in range(width):
            n_img[i,j]=img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
    return n_img

def toBinary(img,threshold):
    height, width = img.shape
    n_img = np.zeros((height, width), np.uint8)
    for i in range(height):
        for j in range(width):
            if img[i,j] >= threshold:
                n_img[i,j] = np.uint8(255)
            else:
                n_img[i,j] = np.uint8(0)
    return n_img

img = cv2.imread("E://resim.png")
cv2.imshow("img",img)
print(type(toGray(img)[1,1]))
cv2.imshow("n_img_gray",toGray(img))
cv2.imshow("n_img_binary", toBinary(toGray(img),125))
cv2.waitKey(0)
