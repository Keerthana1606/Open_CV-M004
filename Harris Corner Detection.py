import cv2
import numpy as np

# Read image
img = cv2.imread('pet.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Apply Harris Corner Detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate result for marking corners
dst = cv2.dilate(dst, None)

# Mark corners in red
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Show image
cv2.imshow('Harris Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()