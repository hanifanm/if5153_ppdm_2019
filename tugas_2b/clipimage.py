import numpy as np
import cv2

def clip (img, container):
    img = np.array(img)
    container = np.array(cv2.cvtColor(container, cv2.COLOR_BGR2GRAY))
    h_img, w_img, col = np.shape(img)
    h_container, w_container = np.shape(container)

    h_max = max(h_img, h_container)
    w_max = max(w_img, w_container)

    for r in range(0, h_max):
        for c in range(0, w_max):
            if(r >= h_container or r >= h_img):
                continue
            if(c >= w_container or c >= w_img):
                continue
            if(container[r][c] > 200):
                img[r][c] = [255, 255, 255]
    return img