import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# Instantiate image grid
fig = plt.figure(constrained_layout=True)

# Image grid dimension specifications
cols = 3  # 3 pictures per row
rows = 10 # number of 3 picture rows. After ten, image grid gets too crowded, or takes too long to create
spec = gridspec.GridSpec(ncols=cols, nrows=rows, figure=fig)

title = []

# Add images 1-9
for img_count in range(9):
    title.append(fig.add_subplot(spec[img_count // cols, img_count % cols]))
    title[-1].set_title("a title for img {}".format(img_count))
    title[-1].set_xticks([])
    title[-1].set_yticks([])
    title[-1].set_xlabel('subplot x axis for img {}'.format(img_count))
    # set global min/ max to get consistent shading
    img_min = 0  # global min for all images in row
    img_max = 100  # global max for all images in row
    plt.imshow(gen_arr, vmin=img_min, mvax=img_max)

# Add grid title and footer at very end, otherwise image looks weird
fig.suptitle('a title')
fig.supxlabel('a footer', size='x-small')
# Save image grid
plt.savefig(os.path.join('path/to/save/loc', 'image_name.png'))
