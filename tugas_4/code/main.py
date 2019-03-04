import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('building.jpg')
img = cv2.imread('lena_noise.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (3,3), 0)

canny = cv2.Canny(blur, 175, 175)
laplacian = cv2.Laplacian(blur, cv2.CV_64F, ksize=5)
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=5)

plt.figure(1)
plt.subplot(321), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322), plt.imshow(blur, cmap='gray'), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(canny, cmap='gray'), plt.title('Canny')
plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(laplacian, cmap='gray'), plt.title('Laplace')
plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])
plt.suptitle('Edge Detection', size=14)
plt.savefig('Result')
    
plt.show()