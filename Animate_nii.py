# coding: utf-8
"""
Created on Tue Apr 13 12:06:54 2021

@author: Sara Kassani
"""

import os
from glob import glob

import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

nii_path = "data/Training Batch 1/"

all_images=glob(os.path.join(nii_path,"volume-*.nii"))
all_masks=glob(os.path.join(nii_path,"segmentation-*.nii"))


first_image=nib.load(all_images[2]).get_fdata()
first_mask=nib.load(all_masks[2]).get_fdata()





def init_ims():
    ims1 = []
    ims2 = []
    return (ims1, ims2 )

def animate1(i):
    im = ax1.imshow(first_image[i], animated=True)
    ims1.append(im)
    return (ims1, )


fig, ax1= plt.subplots(1, figsize = (12, 6))

ax1.set_title('Image')

ims1 = []

anim = animation.FuncAnimation(fig, animate1, init_func=init_ims, frames=100, interval=10)

rc('animation', html='jshtml')
rc

HTML(anim.to_jshtml())



def animate2(i):
    im = ax2.imshow(first_mask[i], animated=True)
    ims2.append(im)
    return ims2



fig, ax2 = plt.subplots(1, figsize = (12, 6))
ax2.set_title('Mask')

ims2 = []
anim = animation.FuncAnimation(fig, animate2, init_func=init_ims, frames=100, interval=10)

rc('animation', html='jshtml')
rc

HTML(anim.to_jshtml())