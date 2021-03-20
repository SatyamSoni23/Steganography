# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:59:19 2021

@author: DELL
"""

import numpy as np
import cv2
import csv

encrypt_img = cv2.imread('Encrypted Image.png', cv2.IMREAD_COLOR)
key_img = cv2.imread('key_text_qr_code.png', cv2.IMREAD_COLOR)

m, n = encrypt_img.shape[:2]


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


"""---------------------- Importing Initial Permutation -----------------"""

permute = open('Initial_Permutation.csv', 'r')
intial_permute = csv.reader(permute, delimiter = ',')
intial_permute_data = []
for i in intial_permute:
    intial_permute_data.append(i)

"""-----------------------------------------------------------------------"""

"""============================ Encryption ==============================="""

"""--------------------------- Encrypting Color --------------------------"""

def encryption_color(plain_img):
    for i in range(0, m):
        for j in range(0, n):
            r, g, b = plain_img[i, j]
            x = int(red_data[i][j])
            y = int(green_data[i][j])
            z = int(blue_data[i][j])
            r = r^x
            g = g^y
            b = b^z
            plain_img[i, j] = r, g, b
    return plain_img          

"""---------------------------- Shuffle pixel ----------------------------"""
def shuffle_pixel(plain_img):
    encrypted_img = np.zeros(shape=[525,525,3], dtype=np.uint8)
    for i in range(0, m):
        for j in range(0, n):
            val = int(intial_permute_data[i][j])
            row = int(val/n)
            col = val%n;
            encrypted_img[i, j] = plain_img[row, col]
    return encrypted_img

"""---------------------------- Plain_key_xor ----------------------------"""
def plain_key_xor(plain_img, key_img):
    img = np.zeros(shape=[525,525,3], dtype=np.uint8)
    for i in range(0, m):
        for j in range(0, n):
            img[i, j] = plain_img[i, j] ^ key_img[i, j]
    return img


"""---------------------- Drive Code for Encryption ----------------------"""

def qr_encryption(plain_img):
    plain_img = encryption_color(plain_img) 
    encrypted_img = shuffle_pixel(plain_img)
    return encrypted_img

encrypted_key_img = qr_encryption(key_img)

#encrypted_img = plain_key_xor(encrypted_img, encrypted_key_img)

"""======================================================================="""

"""=========================== Decryption ================================"""

"""--------------------------- Decrypting Color --------------------------"""
def shuffle_decrypt(encrypted_img):
    decrypt_shuffle = np.zeros(shape=[525,525,3], dtype=np.uint8)
    for i in range(0, m):
        for j in range(0, n):
            val = int(intial_permute_data[i][j])
            row = int(val/n)
            col = val%n;
            decrypt_shuffle[row, col] = encrypted_img[i, j]
    return decrypt_shuffle


"""--------------------------- Decrypting shuffle ------------------------"""
def decryption_color(decrypt_shuffle):
    decrypted_img = np.zeros(shape=[525,525,3], dtype=np.uint8)
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
    return decrypted_img


"""----------------------- Drive Code for Decryption ---------------------"""
def qr_decryption(encrypted_img):
    decrypt_shuffle = shuffle_decrypt(encrypted_img)
    decrypted_img = decryption_color(decrypt_shuffle)
    return decrypted_img

def rounds(encrypt_img, encrypted_key_img):
    decrypted_img = plain_key_xor(encrypt_img, encrypted_key_img)
    decrypted_img = qr_decryption(decrypted_img)
    decrypted_key_img = qr_decryption(encrypted_key_img)
    return decrypted_img, decrypted_key_img

#decrypted_img, decrypted_key_img = rounds(encrypt_img, encrypted_key_img)
decrypted_img = encrypt_img
decrypted_key_img = encrypted_key_img
for i in range(0, 10):
    plain_image = np.zeros(shape=[525,525,3], dtype=np.uint8)
    key_image = np.zeros(shape=[525,525,3], dtype=np.uint8)
    plain_image, key_image = rounds(decrypted_img, decrypted_key_img)
    decrypted_img = np.zeros(shape=[525,525,3], dtype=np.uint8)
    decrypted_key_img = np.zeros(shape=[525,525,3], dtype=np.uint8)
    decrypted_img = plain_image
    decrypted_key_img = key_image

"""======================================================================="""


"""--------------------------------- Output ------------------------------"""

cv2.imwrite('Decrypted Image.png', decrypted_img)
cv2.imshow('Decrypted Image.png', decrypted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""-----------------------------------------------------------------------"""