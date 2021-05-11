# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:10:13 2021

@author: Dipen
"""

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('./data.png')

result = decode(img)

print(result)