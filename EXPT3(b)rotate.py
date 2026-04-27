import cv2

img = cv2.imread("pet.jpg")

(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Rotate by 45 degrees
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
