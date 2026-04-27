import cv2

img = cv2.imread("Food delivery.png")

# Crop (y1:y2, x1:x2)
crop = img[100:300, 150:400]

cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
