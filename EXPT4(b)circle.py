import cv2

img = cv2.imread("Bear.jpg")

# Draw rectangle (top-left, bottom-right, color, thickness)
cv2.rectangle(img, (50, 50), (300, 200), (0, 255, 0), 3)

# Draw circle (center, radius, color, thickness)
cv2.circle(img, (200, 300), 80, (0, 0, 255), 3)

cv2.imshow("Rectangle & Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
