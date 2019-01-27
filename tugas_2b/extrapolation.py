import numpy as np

def extrapolate(img):
    img = np.array(img)
    height, width, color = np.shape(img)
    bigimg = np.zeros((height * 2 - 1, width * 2 - 1, 3), dtype=np.uint8)

    for r in range(height):
        for c in range(width):
            bigimg[r * 2, c * 2] = img[r][c]

    # Fill horizontal
    for r in range(height - 1):
        for c in range(width - 1):
            px1 = bigimg[r * 2, c * 2]
            px2 = bigimg[r * 2, c * 2 + 2]
            avg = np.average([px1, px2], axis=0)
            bigimg[r * 2, c * 2 + 1] = avg

    # Fill Vertical
    for r in range(height - 1):
        for c in range(width * 2 - 1):
            px1 = bigimg[r * 2, c]
            px2 = bigimg[r * 2 + 2, c]
            avg = np.average([px1, px2], axis=0)
            bigimg[r * 2 + 1, c] = avg

    return bigimg