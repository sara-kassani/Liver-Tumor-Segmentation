# coding: utf-8
"""
Created on Tue Apr 13 11:30:03 2021

@author: Sara Kassani
"""

import SimpleITK as sitk
import warnings
warnings.filterwarnings("always")
warnings.filterwarnings("ignore")



file_path = "data/Training Batch 1/volume-0.nii"
img = sitk.ReadImage(file_path)
img_array = sitk.GetArrayFromImage(img)
img_array.shape

# number of slices, height, width