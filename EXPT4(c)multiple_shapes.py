import cv2
import numpy as np
# Create blank white image
img = np.ones((500, 500, 3), dtype="uint8") * 255
# Line
cv2.line(img, (0, 0), (500, 500), (255, 0, 0), 2)
# Rectangle
cv2.rectangle(img, (50, 50), (200, 150), (0, 255, 0), 3)
# Circle
cv2.circle(img, (350, 150), 50, (0, 0, 255), 3)
# Ellipse
cv2.ellipse(img, (250, 350), (100, 50), 0, 0, 360, (255, 255, 0), 2)
# Polygon
pts = np.array([[100,300], [200,250], [300,300], [250,400], [150,400]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 3)
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
