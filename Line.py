import cv2

# Create a blank image
img = cv2.imread("Bear.jpg")
resized = cv2.resize(img, (400,300), interpolation=cv2.INTER_AREA)

# Draw a line (start_point, end_point, color, thickness)
cv2.line(img, (50, 50), (300, 300), (255, 0, 0), 3)

cv2.imshow("Line Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()