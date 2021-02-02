# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:42:19 2021

@author: yigit
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from numpy import asarray
from scipy.ndimage import rotate

# Read Images
star = Image.open('StarMap.png')
small = Image.open('Small_area.png')
small_rtd = Image.open('Small_area_rotated.png')

def find_kernel(star, small):
    
    # Convert Image to Array    
    star_array = asarray(star)
    small_array = asarray(small)
    
    # Convert to 2d and Get size of arrays
    star_2d = star_array[:,:,0]
    y_star, x_star = star_array.shape[0], star_array.shape[1]

    
    small_2d = small_array[:,:,0]
    y_small, x_small = small_array.shape[0], small_array.shape[1]

    m="" 
    points=[]
    for n in ['Not Mirror', 'Transpose', (0,1), 0, 1]:
        
        if n == 'Not Mirror':
            fliped_small = small_2d
            m='Original image'
        elif n == 'Transpose':
            fliped_small = np.transpose(small_2d)
            m="Transpose"
        else:
            fliped_small = np.flip(small_2d, axis=n)
            if n==(0,1):
                m='Mirror image by origin'
            elif n==0:
                m='Mirror by x-axis'
            elif n==1:
                m='Mirror by y-axis'
        for i in range(4):            
            rotated_small = np.rot90(fliped_small,i)
            print('Mirror status: ', m, ' - Rotation number: ', i)
 
            
            xstop = x_star - x_small +1
            ystop = y_star - y_small +1
            for xmin in range(0,xstop):
                for ymin in range(0,ystop):
                    
                    xmax = xmin + x_small
                    ymax = ymin + y_small
                
                    kernel = star_2d[ymin:ymax, xmin:xmax]
                    
                    kernel = np.array(kernel)
                    rotated_small = np.array(rotated_small)
                    comparison = kernel == rotated_small
                    mybool = comparison.all()
                    
                    if mybool:
                        
                        points.append((xmin,ymin))
                        points.append((xmax,ymin))
                        points.append((xmin,ymax))
                        points.append((xmax,ymax))
                        
                        return print(points)
    return print('not found')                

find_kernel(star,small)
