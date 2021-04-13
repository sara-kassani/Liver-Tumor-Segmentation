# coding: utf-8
"""
Created on Mon Apr 12 22:40:39 2021

@author: Sara Kassani
"""

import os  
import nibabel as nib  
import cv2
import numpy as np

def nii_to_image():
    filenames = os.listdir(filepath)
    
    for f in filenames:
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)
        img_fdata = img.get_fdata()
#         print(img_fdata.dtype)  # float64
#         print(np.min(img_fdata), np.max(img_fdata))

        fname = f.replace('.nii', '')  
        img_f_path = os.path.join(imgfile, fname)

        if not os.path.exists(img_f_path):
   
            os.mkdir(img_f_path)  

        (x, y, z) = img.shape
        # z is the sequence of images
        for i in range(z):
            # Choose which direction to slice
            silce = img_fdata[:, :, i]
            silce *=255.0
            silce = silce.astype(np.float64)  
            cv2.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce*255)
            
filepath = 'data/small/'
imgfile = 'data/pngs/'
nii_to_image()