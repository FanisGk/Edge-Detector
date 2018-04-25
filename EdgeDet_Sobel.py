#Name: Fanis Gkaragkanis
#AM: 2422
#Edge Detection with Sobel Filter
import sys
import numpy as np
from scipy.misc import imread, imsave
from scipy.signal import convolve2d

def find_average(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3

def convert_to_grayscale(img):
    gray = np.zeros((img.shape[0], img.shape[1]))  #init 2D numpy array with zeros
    for i in range (len(img)):
        for j in range (len(img[i])):
            gray[i][j] = find_average(img[i][j])
    return gray

def sobel_filter(img, thr):
    kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    gx = convolve2d(img, kernel_x, mode='same', boundary = 'symm')
    gy = convolve2d(img, kernel_y, mode='same', boundary = 'symm')
    mag = np.sqrt(gx * gx + gy * gy)
    thr = float(thr) * np.max(mag)
    mag[mag<=thr]=0
    return mag

image = imread(sys.argv[1]) #load image
threshold = sys.argv[2]
if (float(threshold) >= 1 or float(threshold) <= 0):
    print("Threshold must be in (0,1)\nExiting...")
    sys.exit()

# check if image is RGB
if (len(image.shape) == 3):
    image = convert_to_grayscale(image)
#apply sobel filter to the image
image = sobel_filter(image, threshold)
imsave('result.jpg', image)
