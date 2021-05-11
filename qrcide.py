# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:52:56 2021

@author: Dipen
"""
import qrcode

data = input("Enter data")

qr = qrcode.QRCode(version =1,box_size=10,border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="white")

img.save('./'+data+'.png')