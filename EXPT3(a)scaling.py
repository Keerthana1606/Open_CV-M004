import cv2

img = cv2.imread("pet.jpg")

# Resize using scaling factors (fx, fy)
resized = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
