# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:40:49 2021

@author: Dipen
"""

import random
print("''''''''''''''''''''''")
print('passsword Generator')
print("'''''''''''''''''''''''")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890*/-+;'\][`!@#$%^&*()_+"

number = input("amounts of password to generate: ")
number = int(number)

length = input("input your password length")
length = int(length)


print('\nhere are your passwords: ')

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)




