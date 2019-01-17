import cv2
 
# Convert Image
maudy_ori = cv2.imread('./maudy.jpg')
maudy_gray = cv2.cvtColor(maudy_ori, cv2.COLOR_BGR2GRAY)
maudy_binary = cv2.threshold(maudy_gray, 127, 255, cv2.THRESH_BINARY)[1]
maudy_bgr = cv2.cvtColor(maudy_ori, cv2.COLOR_RGB2BGR)
maudy_hsv = cv2.cvtColor(maudy_ori, cv2.COLOR_RGB2HSV)
maudy_hsv_2 = cv2.cvtColor(maudy_ori, cv2.COLOR_BGR2HSV)

# Show Image
cv2.imshow('Original image',maudy_ori)
cv2.imshow('Gray image', maudy_gray)
cv2.imshow('BW image', maudy_binary)
cv2.imshow('BGR image', maudy_bgr)
cv2.imshow('HSV image', maudy_hsv)
cv2.imshow('HSV 2 image', maudy_hsv_2)

# Save Image
cv2.imwrite('maudy_gray.jpg',maudy_gray)
cv2.imwrite('maudy_binary.jpg',maudy_binary)
cv2.imwrite('maudy_bgr.jpg',maudy_bgr)
cv2.imwrite('maudy_hsv.jpg',maudy_hsv)
cv2.imwrite('maudy_hsv_2.jpg',maudy_hsv_2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()