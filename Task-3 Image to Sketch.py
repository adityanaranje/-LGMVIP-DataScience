# Importing Opencv Library
import cv2

# Importing image
image = cv2.imread('nature.jpg')
cv2.imshow('Original Image', image)

# Converting original image to gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Converting gray scale to inverted image
inverted = cv2.bitwise_not(gray)

# Blurring inverted image using median blur of kernal size 3
blur = cv2.medianBlur(inverted, 3)

# Dividing gray scale image by blurred image
sketch = gray/blur

cv2.imshow("Sketch", sketch)

cv2.waitKey(0)
