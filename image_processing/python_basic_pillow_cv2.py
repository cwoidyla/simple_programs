import numpy as np
from PIL import Image
import cv2

path_to_img = "/path/to/img"
path_to_new_img = "/path/to/new/img"

pil = Image.open(path_to_img)
np_arr = np.array(pil)

# convert to RGB if not RGB
np_arr = cv2.cvtColor(np_arr, cv2.COLOR_GRAY2RGB)

# Save as RGB
img = Image.fromarray(np_arr, "RGB")
img.save()

# read and convert images to grayscale
cv2.imread(path_to_img, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(path_to_new_img, np_arr)

