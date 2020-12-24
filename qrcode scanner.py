# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:34:53 2020

@author: DELL
"""

import cv2 as cv

im = cv.imread('Decrypted Image.png')
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
print(retval)