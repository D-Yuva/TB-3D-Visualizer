import numpy as np

def extrude_2d_to_3d(masked_image, depth=30):
    height, width = masked_image.shape
    volume = np.zeros((depth, height, width), dtype=np.uint8)

    for i in range(depth):
        volume[i] = masked_image

    return volume
