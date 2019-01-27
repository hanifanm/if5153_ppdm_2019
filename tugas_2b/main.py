from pixelsorting import sortpixel
import cv2

img = cv2.imread('./sunflower.jpg')
img_sorted = sortpixel(img)
cv2.imshow('Sunflower', img_sorted)

cv2.waitKey(0)
cv2.destroyAllWindows()