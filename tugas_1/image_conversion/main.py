import cv2
 
image = cv2.imread('./maudy.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
# hsl = cv2.cvtColor(image, cv2.COLOR_RGB2HSL)
 
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
cv2.imshow('BW image', binary)
cv2.imshow('BGR image', bgr)
cv2.imshow('HSV image', hsv)
# cv2.imshow('HSL image', hsl)
 
cv2.waitKey(0)
cv2.destroyAllWindows()