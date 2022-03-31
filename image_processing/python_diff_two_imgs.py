import os
import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser(description="")
parser.add_argument("-i1", "--image1", help="first image", type=str, required=True)
parser.add_argument("-i2", "--image2", help="second image", type=str, required=True)
parser.add_argument("-o", "--output", help="set output PNG filename", type=str, default="image_diff.png")
args = parser.parse_args()

# Read and convert images to grayscale
img1 = cv2.imread(args.i1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(args.i2, cv2.IMREAD_GRAYSCALE)

# Find differences in img1's and img2's pixels
diff = np.subtract(img1, img2)
diff_img = np.empty_like(diff)

# assign gradient values if difference is detected
diff_img[diff <= 255] = 255
diff_img[diff <= 128] = 128
diff_img[diff <= 64] = 64
diff_img[diff <= 16] = 16
diff_img[diff <= 1] = 1
diff_img[diff <= 0] = 0

# Visualize image diffs
cv2.imwrite("/path/to/img_diff.png", diff_img)