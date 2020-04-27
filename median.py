import cv2
import numpy as np
import random
import math
img = cv2.imread("cameraman.tif")
cv2.imshow("img",img)
cv2.waitKey(0)
print(img.shape)
height, width, channel = img.shape
b=int(input("Blok boyutunu giriniz: "))
new_img=img
for i in range(width-b-1):
    for j in range(height-b-1):
        
        x=img[i:i+b-1,j:j+b-1]
        
        t=np.transpose(x)
        print(t)
        st=np.sort(t)
        print(np.sort(t))
        indis=math.ceil(b*(b/2))
  
        new_img[i+1,j+1]=st[indis]
cv2.imshow("n",new_img)