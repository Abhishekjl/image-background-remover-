# -*- coding: utf-8 -*-
"""mine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-2RFb0QL2vr5mHZtAkoXJDczFq6SLUbB

#### Changing Background using pretrained Unet model
* here i will  be using the fastest and accurate way to change background 
* we can use pytorch as well to do this task more precisely 
* in this notebook i will replace the background with black color 
* this  is  an assignment task for Carscan internship 
* Author: Abhishek Jaiswal
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content

!git clone https://github.com/shreyas-bk/U-2-Net

# %cd /content/U-2-Net
!mkdir images

print('making images directory')
print('making results directory')
!mkdir results
print('importing...')
from google.colab import files
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image as Img
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
print('Done')

"""#### Lets upload images """

# Commented out IPython magic to ensure Python compatibility.
# upload cell
# %cd /content/U-2-Net/images
uploaded = files.upload()
# %cd /content/U-2-Net

img = Image.open('/content/U-2-Net/images/view3.jpeg')
display(img)

#### now its time to create a mask 
!ls
!python -W ignore u2net_test.py

mask = cv2.imread('/content/U-2-Net/results/view3.png')
# mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
cv2_imshow(mask)

mask.shape

masked = cv2.bitwise_and(np.array(img),np.array(mask))
cv2_imshow(masked)

cv2.imwrite('view3_black_background.jpeg',masked)

