import cv2

# Load image (OpenCV loads in BGR by default)
img = cv2.imread('pet.jpg')

# BGR to RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display images
cv2.imshow("Original (BGR)", img)
cv2.imshow("RGB Image", rgb_img)
cv2.imshow("Grayscale Image", gray_img)
cv2.imshow("HSV Image", hsv_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
