# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:23:09 2020

@author: Satyam Soni
"""
from pytesseract import image_to_string
import numpy as np
import cv2
img = cv2.imread('abc.png', cv2.IMREAD_COLOR)
key = input("Enter Password")
s = len(key)
print(s)
k = 0
m, n = img.shape[:2]
for i in range(1, m):
    for j in range(1, n):
        r, g, b = img[i, j]
        if i%2 == 0 and j%2 == 0:
            r = (r^255)
        elif i%2 == 0 or j%2 == 0:
            g = (g^127)
        else:
            b = (b^255)
        img[i, j] = r, g, b
for i in range(1, m):
    for j in range(1, n):
        r, g, b = img[i, j]
        if i%2 == 0 and j%2 == 0:
            y = ord(key[k]) - ord('0')
            r = (r^y)
        elif i%2 == 0 or j%2 == 0:
            y = ord(key[k]) - ord('0')
            g = (g^y)
        else:
            y = ord(key[k]) - ord('0')
            b = (b^y)        
        k = (k+1)%s
        img[i, j] = r, g, b
        
def imageToText(img):
    try :
        return image_to_string(img)
    except IOError :
        return "Enter the correct path"

blank_img = np.zeros(shape=[100,300,3], dtype=np.uint8)

for x in range(1, m):
    for y in range(1, n):
        blank_img[x, y] = img[x, y]

print(imageToText(img))

#0print(img)
cv2.imshow('image',blank_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
