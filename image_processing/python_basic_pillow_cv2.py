import numpy as np
from PIL import Image
import cv2

path_to_img = "/path/to/img"
path_to_new_img = "/path/to/new/img"

# Read image
pil = Image.open(path_to_img)
np_arr = np.array(pil)

# convert to RGB if not RGB
np_arr = cv2.cvtColor(np_arr, cv2.COLOR_GRAY2RGB)

# Save as RGB
img = Image.fromarray(np_arr, "RGB")
img.save(path_to_new_img)

# read and convert images to grayscale
cv2.imread(path_to_img, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(path_to_new_img, np_arr)

# Make a circle!
height = 100
width = 100
channel = 3
circ_arr = np.zeros((height, width, channel), dtype=np.float32)
circle_padding = 10  # concentric circle density
num_circles = ((height + width) // 2) // circle_padding  # number of circles relative to height/width/circle_padding
for i in range((num_circles)):
    center = (width // 2, height // 2)
    radius = i * circle_padding
    color = (128, 128, 128)  # RGB for gray
    thickness = 1
    cv2.circle(circ_arr, center, radius, color, thickness)  # cv2.circle populates np zeroes array

img = Image.fromarray(circ_arr, "RGB")
img.save(path_to_new_img)
# OR
cv2.imwrite(path_to_new_img, np_arr)
