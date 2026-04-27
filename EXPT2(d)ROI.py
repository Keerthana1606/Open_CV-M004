import cv2

# Read image
img = cv2.imread("Food delivery.png")

# Define ROI (y1:y2, x1:x2)
roi = img[100:300, 150:400]

# Show ROI
cv2.imshow("ROI", roi)

# Optional: place ROI somewhere else
img[0:200, 0:250] = roi

cv2.imshow("Modified Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
