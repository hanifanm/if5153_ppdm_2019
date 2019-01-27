from pixelsorting import sortpixel
from clipimage import clip
from extrapolation import extrapolate
import numpy as np
import cv2

sunflower = cv2.imread('./sunflower.jpg')
diamond = cv2.imread('./diamond.jpeg')
eiffel = cv2.imread('./eiffel_mini.jpg')

# 1
image1 = sunflower

img_sorted = sortpixel(image1)
result1 = np.concatenate((image1, img_sorted), axis=1)
cv2.imshow('Pixel Sorting', result1)
cv2.imwrite('PixelSorting.jpg', result1)

# 2
image2_main = sunflower
image2_container = diamond

clipped = clip(image2_main, image2_container)
result2 = np.concatenate((image2_main, image2_container, clipped), axis=1)
cv2.imshow('Image Clip', result2)
cv2.imwrite('ImageClip.jpg', result2)

# 3
image3 = eiffel

extrapolated = extrapolate(image3)
image3_h, image3_w, image3_c = np.shape(image3)
extrapolated_h, extrapolated_w, extrapolated_c = np.shape(extrapolated)
temp = np.ones((extrapolated_h, image3_w, 3), dtype=np.uint8) * 255
temp[0:image3_h] = image3
result3 = np.concatenate((temp,extrapolated), axis=1)
cv2.imshow('Extrapolation', result3)
cv2.imwrite('Extrapolation.jpg', result3)

cv2.waitKey(0)
cv2.destroyAllWindows()