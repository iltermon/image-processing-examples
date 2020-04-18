import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(img):
    height, width = img.shape
    hist=np.zeros((256,1))
    for i in range(width):
        for j in range(height):
            hist[img[i,j]+1]=hist[img[i,j]+1]+1
    return hist
img = cv2.imread('E:\\cameraman.tif',0)
cv2.imshow("img",img)
plt.plot(histogram(img))
plt.show()
cv2.waitKey(0)