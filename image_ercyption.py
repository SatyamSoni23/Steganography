# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:23:09 2020

@author: Satyam Soni
"""

from pytesseract import image_to_string
import numpy as np
import cv2
import csv

img = cv2.imread('abc.jpg', cv2.IMREAD_COLOR)
key = input("Enter Password\n")
s = len(key)
print(s)
k = 0
m, n = img.shape[:2]


"""------------------------ Importing Color S Box ------------------------"""
red = open('Red_S_Box.csv', 'r')
green = open('Green_S_Box.csv', 'r')
blue = open('Blue_S_Box.csv', 'r')

red_arr = csv.reader(red, delimiter = ',')
green_arr = csv.reader(green, delimiter = ',')
blue_arr = csv.reader(blue, delimiter = ',')

red_data = []
green_data = []
blue_data = []

for i in red_arr:
    red_data.append(i)

for i in green_arr:
    green_data.append(i)

for i in blue_arr:
    blue_data.append(i)
    
"""----------------------------------------------------------------------"""


"""---------------------- Importing Initial Permutation -----------------"""

permute = open('Intial_Permutation.csv', 'r')
intial_permute = csv.reader(permute, delimiter = ',')
intial_permute_data = []
for i in intial_permute:
    intial_permute_data.append(i)

"""-----------------------------------------------------------------------"""


"""--------------------------- Encrypting Color --------------------------"""

for i in range(0, m):
    for j in range(0, n):
        r, g, b = img[i, j]
        x = int(red_data[i][j])
        y = int(green_data[i][j])
        z = int(blue_data[i][j])
        r = r^x
        g = g^y
        b = b^z
        img[i, j] = r, g, b
        
"""-----------------------------------------------------------------------""" 


"""---------------------------- Shuffle pixel ----------------------------"""
encrypted_img = np.zeros(shape=[100,300,3], dtype=np.uint8)
for i in range(0, m):
    for j in range(0, n):
        val = int(intial_permute_data[i][j])
        row = int(val/n)
        col = val%n;
        encrypted_img[i, j] = img[row, col]
"""-----------------------------------------------------------------------"""


"""--------------------------- Decrypting Color --------------------------"""
decrypt_shuffle = np.zeros(shape=[100,300,3], dtype=np.uint8)
for i in range(0, m):
    for j in range(0, n):
        val = int(intial_permute_data[i][j])
        row = int(val/n)
        col = val%n;
        decrypt_shuffle[row, col] = encrypted_img[i, j]

decrypted_img = np.zeros(shape=[100,300,3], dtype=np.uint8)
for i in range(0, m):
    for j in range(0, n):
        r, g, b = decrypt_shuffle[i, j]
        x = int(red_data[i][j])
        y = int(green_data[i][j])
        z = int(blue_data[i][j])
        r = r^x
        g = g^y
        b = b^z
        decrypted_img[i, j] = r, g, b
"""-----------------------------------------------------------------------""" 


"""---------------------------- Image to text ----------------------------"""
def imageToText(img):
    try :
        return image_to_string(img)
    except IOError :
        return "Enter the correct path"
print(imageToText(decrypted_img))
"""-----------------------------------------------------------------------"""


"""--------------------------------- Output ------------------------------"""
cv2.imshow('Encrypted',encrypted_img)
cv2.imshow('Decrypted', decrypted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""-----------------------------------------------------------------------"""