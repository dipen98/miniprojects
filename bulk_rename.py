# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:44:30 2021

@author: Dipen
"""

import os
def main():
    
    i = 0
    path = "C:/Users/dipen/Documents/"
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
        
        
if __name__ == '__main__':
    main()
