import cv2
from matplotlib import pyplot as plt

# Declare Equalize Function
def equalizeHist(img):
    res = img.copy()
    for c in range(0, 2):
       res[:,:,c] = cv2.equalizeHist(res[:,:,c])
    return res

def adaptiveEqualizeHist(img):
    res = img.copy()
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    for c in range(0, 2):
        res[:,:,c] = clahe.apply(res[:,:,c])
    return res

# Declare Histogram Function
def plotHist(img):
    color = ('r','g','b')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr, color = col, linewidth=0.7)
        plt.xlim([0,256])
 
# Load Image
mainTitle = 'Maudy'
img = plt.imread('./maudy.jpg') # image loaded using RGB color scheme

# Histogram Equalization
equ = equalizeHist(img)
ahe = adaptiveEqualizeHist(img)

plt.figure(1)
plt.subplot(231), plt.imshow(img), plt.axis('off'),
plt.subplot(232), plt.imshow(equ), plt.axis('off'),
plt.subplot(233), plt.imshow(ahe), plt.axis('off'),
plt.subplot(234), plotHist(img), plt.gca().set_title('Original Histogram')
plt.subplot(235), plotHist(equ), plt.gca().set_title('Equalized Histogram')
plt.subplot(236), plotHist(ahe), plt.gca().set_title('Adaptive Eq. Histogram')
plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.suptitle('Histogram Equalization - ' + mainTitle)
plt.savefig('Histogram Equalization - ' + mainTitle, dpi=500)


# Histogram In Multiple Colorspace
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB) # convert back to rgb for histogram analysis
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
plt.figure(2)
plt.subplot(231), plt.imshow(img), plt.axis('off'),
plt.subplot(232), plt.imshow(img_gray), plt.axis('off'),
plt.subplot(233), plt.imshow(img_hsv), plt.axis('off'),
plt.subplot(234), plotHist(img), plt.gca().set_title('Original Histogram')
plt.subplot(235), plotHist(img_gray), plt.gca().set_title('Grayscale Histogram')
plt.subplot(236), plotHist(img_hsv), plt.gca().set_title('HSV Histogram')
plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.suptitle('Histogram Colorspace - ' + mainTitle)
plt.savefig('Histogram Colorspace - ' + mainTitle, dpi=500)

plt.show()