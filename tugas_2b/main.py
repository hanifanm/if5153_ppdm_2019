from pixelsorting import sortpixel
from clipimage import clip
from extrapolation import extrapolate
import cv2

sunflower = cv2.imread('./sunflower.jpg')
diamond = cv2.imread('./diamond.jpeg', 0)
eiffel = cv2.imread('./eiffel_mini.jpg')

# 1
# img_sorted = sortpixel(sunflower)
# cv2.imshow('Sunflower', sunflower)
# cv2.imshow('Sorted', img_sorted)

# 2
# clipped = clip(sunflower, diamond)
# cv2.imshow('Clip', clipped)

# 3
extrapolated = extrapolate(eiffel)
cv2.imshow('Eiffel Bix', extrapolated)
cv2.imwrite('Eiffel Big.jpg',extrapolated)

cv2.waitKey(0)
cv2.destroyAllWindows()