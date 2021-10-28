# TASK 1 : Use any 3 functions/modules in OpenCV,
# and commit the code in the official Expressando TDoC 2021 Repository.


# Importing Modules
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Reading images and Resizing it as per needs

img = cv.imread('image.jpg')
width, height = int(img.shape[1] / 2.5), \
                int(img.shape[0] / 2.5)  # Dynamically allotting the width and height of the image

img = cv.resize(img, (width, height), cv.INTER_CUBIC)  # Resizing the image as per our need

cv.imshow('Flower - Original', img)

# ------------------------ + OPERATIONS ON THE IMPORTED IMAGE + ---------------------------------------------------

# 1. Grayscaling the Image
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscaled Image', img_grey)

# 2. Bluring Image
img_blur_simple = cv.blur(img, (5, 5))
img_blur_Gaussian = cv.GaussianBlur(img, (5, 5), 0)
# cv.imshow('Simple Blur Image', img_blur_simple)
# cv.imshow('Gaussian Blur Image', img_blur_Gaussian)


titles = ['Original Image', 'Gray Scale', 'Simple Blur Image', 'Gaussian Blur Image']
images = [img, img_grey, img_blur_simple, img_blur_Gaussian]

# Displaying the ORIGINAL IMAGE, GRAY SCALE IMAGE, SIMPLE BLUR IMAGE, GAUSSIAN BLUR IMAGE
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# 3. Simple Threshold
img_gfg = cv.imread('gfg.jpg', 1)
img_gfg_grey = cv.cvtColor(img_gfg, cv.COLOR_BGR2GRAY)

ret_1, img_thresh1 = cv.threshold(img_gfg_grey, 120, 255, cv.THRESH_BINARY)
ret_2, img_thresh2 = cv.threshold(img_gfg_grey, 120, 255, cv.THRESH_BINARY_INV)
ret_3, img_thresh3 = cv.threshold(img_gfg_grey, 120, 255, cv.THRESH_TOZERO)
ret_4, img_thresh4 = cv.threshold(img_gfg_grey, 120, 255, cv.THRESH_TOZERO_INV)
ret_5, img_thresh5 = cv.threshold(img_gfg_grey, 120, 255, cv.THRESH_TRUNC)

# cv.imshow('Original', img_gfg)
# cv.imshow('Binary Thresh', img_thresh1)
# cv.imshow('Binary Inverse Thresh', img_thresh2)
# cv.imshow('Tozero Thresh', img_thresh3)
# cv.imshow('Tozero Inverse Thresh', img_thresh4)
# cv.imshow('Trunc Thresh', img_thresh5)

# Displaying the ORIGINAL IMAGE, BINARY THRESHOLD IMAGE, BINARY INVERSE THRESHOLD IMAGE,
# TOZERO IMAGE, TOZERO INVERSE IMAGE, TRUNC IMAGE
titles = ['Original Image', 'Binary Thresh', 'Binary Inverse Thresh', 'Tozero Thresh', 'Tozero Inverse Thresh',
          'Trunc Thresh']
images = [img_gfg_grey, img_thresh1, img_thresh2, img_thresh3, img_thresh4, img_thresh5]

for i in range(6):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
