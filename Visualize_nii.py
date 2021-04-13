# coding: utf-8
"""
Created on Tue Apr 13 11:34:31 2021

@author: Sara Kassani
"""

import skimage, os
from glob import glob

import nibabel as nib
from skimage.util import montage
import matplotlib.pyplot as plt

nii_path = "data/Training Batch 1/"

all_images=glob(os.path.join(nii_path,"volume-*.nii"))
all_masks=glob(os.path.join(nii_path,"segmentation-*.nii"))
print('Total number of images & Total number of masks:', len(all_images), len(all_masks))

first_image=nib.load(all_images[2]).get_fdata()
first_mask=nib.load(all_masks[2]).get_fdata()

first_image.shape


x1, y1, z1 = first_image.shape
x2, y2, z2 = first_mask.shape
print('first image dimension', x1, y1, z1)
print('first mask dimension',  x2, y2, z2)


fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12, 10))

# show first image
ax1.imshow(first_image[z1//2]) 
ax1.set_title('Image')

# show first mask
ax2.imshow(first_mask[z2//2])
ax2.set_title('Mask')




fig, ax1 = plt.subplots(1, 1, figsize = (20, 20))
ax1.imshow(montage(first_image), cmap ='bone')


