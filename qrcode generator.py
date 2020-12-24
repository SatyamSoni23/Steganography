# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:22:28 2020

@author: DELL
"""

import qrcode

qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=20,
)
plain_text = input('Enter the Plain Text\n')
qr.add_data(plain_text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

img.save("qrcode.png")