import numpy as np

def sortpixel(img_ori):
    img = np.array(img_ori)
    height, width, c = np.shape(img)
    img.shape = (height*width, c)

    # Add forth column, R + G + B
    res = np.zeros((height*width, 4), dtype=np.uint8)
    res[:, 0:3] = img
    res[:, c] = np.sum(img[:,0:3], axis=1)

    # Sort based on the sum
    ind=np.argsort(res[:,-1])
    res=res[ind]

    img = res[:, 0:3]
    img.shape = (height, width, c)
    return img