import cv2

# Read image
img = cv2.imread("Food delivery.png")

# Resize to specific size (width, height)
resized = cv2.resize(img, (400, 300))

cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()