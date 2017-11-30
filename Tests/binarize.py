import cv2
import numpy as np
from matplotlib import pyplot as plt
#color_img = cv2.imread('C:/Users/Administrator/Desktop/imageProcess/test.jpeg',1)

color_img = cv2.imread('C:/Users/Administrator/Desktop/imageProcess/test2.png',1)

gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

img=gray_img
# cv2.imwrite('test_g.jpg',gray_img)

# cv2.imshow('color_img',color_img)             
# cv2.imshow('gray_img',gray_img)

# img=gray_img

thresh1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,5)

#ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2]

# plt.imshow(thresh1,'binary')
# plt.show()

# plt.imshow(thresh2,'binary')
# plt.show()

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()