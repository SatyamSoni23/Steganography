# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:46:20 2020

@author: DELL
"""

import numpy as np
import cv2

img = cv2.imread('abc.png', cv2.IMREAD_COLOR)
#key = input("Enter Password")
#s = len(key)
#print(s)
#k = 0
m, n = img.shape[:2]
red = ""
green = ""
blue = ""
for i in range(1, m):
    for j in range(1, n):
        r, g, b = img[i, j]
        red = red + "&" + str(r)
        green = green + "&" + str(g)
        blue = blue + "&" + str(b)

blank_img = np.zeros(shape=[100,300,3], dtype=np.uint8)

print(red)
print(green)
print(blue)        