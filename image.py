# -*- coding: utf-8 -*-
"""image.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CpCziZ7etOB0FyHT_nYtHDxaVCxlFXg-
"""

from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

img = image.imread('/content/flower.jpg')
print(img)

print(type(img))

plt.imshow(img)

a = img.shape
print(a)

a = img.ndim
print(a)

a = img.size
print(a)

# 183, 275, 3
img1 = img[50:150, 50: 200]
plt.imshow(img1)

img2 = img[:,:, 0]
plt.imshow(img2)

a = np.vstack((img[50:150] , img[50:200]))
plt.imshow(a)

a = np.hstack((img[50:150] , img[0:100]))
plt.imshow(a)

from matplotlib.colors import Normalize
img1 = (img * 500)
norm = Normalize(vmin=img1.min(), vmax=img1.max())
plt.imshow(img1, cmap='gray', norm=norm)
plt.colorbar()

new  = img.copy()
new[:,4,2] = 0
plt.imshow(new)

img1  = np.flip(img)
plt.imshow(img1)

img1  = np.flip(img, axis = 2) #rgb
plt.imshow(img1)

img1 = img[50:150,50:150]
print(img1.size) # 100, 100, 3


img2 = img1.reshape(50,200,3)
plt.imshow(img2)