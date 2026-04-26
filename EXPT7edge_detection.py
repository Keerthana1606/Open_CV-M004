import cv2
import numpy as np

# 1. Read image in grayscale
img = cv2.imread("C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/Lib/site-packages/pet.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found")
    exit()

# 2. Sobel Edge Detection (X and Y)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges

# Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine Sobel X and Y
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# 3. Laplacian Edge Detection
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# 4. Canny Edge Detection
canny = cv2.Canny(img, 100, 200)

# 5. Display all outputs
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
