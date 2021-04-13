# coding: utf-8
"""
Created on Mon Apr 12 22:42:47 2021

@author: Sara Kassani
"""

import os, sys
import pydicom
import nibabel
import cv2
import numpy as np

def nii_to_png(input_path, output_path):
    if not os.path.exists(output_path):
            os.makedirs(output_path)

    file_list = []
    for parent, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            if filename.lower().endswith(('.nii', '.nii.gz', '.dcm')):
                file_list.append(os.path.join(parent, filename))

    for files in file_list:
        if files.lower().endswith('.dcm'):
            image = pydicom.dcmread(files)
            img_name = files.replace('.dcm', '.png')
            cv2.imwrite(img_name, image.pixel_array)

        if files.lower().endswith(('.nii', '.nii.gz')):
            pixel_array = nibabel.load(files).get_fdata()
#             print(pixel_array.shape)
            total_slices = pixel_array.shape[2]
#             print(total_slices)
            for slices in range(0, total_slices):
                image =  pixel_array[:, :, slices]*255
                image = image.astype(np.float64)  
                
                img_name = files.replace('.nii.gz', '_{}.png'.format(slices))
                
                if files.lower().endswith('.nii'):
                    img_name = files.replace('.nii', '_{}.png'.format(slices))
                    
                    file_name = os.path.basename(img_name)
                    dst_name = os.path.join(output_path, file_name)
                    cv2.imwrite(dst_name, image)
                    
input_path = "data/small/"
output_path = "data/pngs/"

nii_to_png(input_path, output_path)