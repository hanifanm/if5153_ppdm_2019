import cv2
import numpy as np
from matplotlib import pyplot as plt

img = plt.imread('lena_noise.png')
noimg = plt.imread('no_image.png')

kernel3 = np.ones((3,3),np.float32)/9
kernel5 = np.ones((5,5),np.float32)/25
kernel7 = np.ones((7,7),np.float32)/49

avg3 = cv2.filter2D(img,-1,kernel3)
avg5 = cv2.filter2D(img,-1,kernel5)
avg7 = cv2.filter2D(img,-1,kernel7)

gauss3 = cv2.GaussianBlur(img, (3,3), 0)
gauss5 = cv2.GaussianBlur(img, (5,5), 0)
gauss7 = cv2.GaussianBlur(img, (7,7), 0)

med3 = cv2.medianBlur(img, 3)
med5 = cv2.medianBlur(img, 5)
med7 = noimg

sigma = 75
bil3 = cv2.bilateralFilter(img,3,sigma,sigma)
bil5 = cv2.bilateralFilter(img,5,sigma,sigma)
bil7 = cv2.bilateralFilter(img,7,sigma,sigma)

def mergeFigure(fIndex, methodName, img1, img3, img5, img7):
    plt.figure(fIndex)
    plt.subplot(221), plt.imshow(img1), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(img3), plt.title('Kernel 3')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(img5), plt.title('Kernel 5')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img7), plt.title('Kernel 7')
    plt.xticks([]), plt.yticks([])
    plt.suptitle('Smoothing : ' + methodName, size=14)
    plt.savefig(methodName)

mergeFigure(1, 'Averaging', img, avg3, avg5, avg7)
mergeFigure(2, 'Gaussian', img, gauss3, gauss5, gauss7)
mergeFigure(3, 'Median', img, med3, med5, med7)
mergeFigure(4, 'Bilateral', img, bil3, bil5, bil7)

plt.show()