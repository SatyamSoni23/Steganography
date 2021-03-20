# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:22:28 2020

@author: DELL
"""

import qrcode

qr_plain = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=20,
)

qr_key = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=20,
)

plain_text = input('Enter the Plain Text\n')
qr_plain.add_data(plain_text)
qr_plain.make(fit=True)
img = qr_plain.make_image(fill_color="black", back_color="white").convert('RGB')
img.save("plain_txt_qr_code.png")

key_text = input('Enter the Key\n')
qr_key.add_data(key_text)
qr_key.make(fit=True)
img = qr_key.make_image(fill_color="black", back_color="white").convert('RGB')
img.save("key_text_qr_code.png")