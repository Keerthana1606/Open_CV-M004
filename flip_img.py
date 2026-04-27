import cv2

img = cv2.imread("Food delivery.png")

# Flip horizontally
horizontal = cv2.flip(img, 1)

# Flip vertically
vertical = cv2.flip(img, 0)

cv2.imshow("Horizontal Flip", horizontal)
cv2.imshow("Vertical Flip", vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()