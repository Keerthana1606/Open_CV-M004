import cv2

# Read image
img = cv2.imread('pet.jpg', 0)

# Create FAST detector
fast = cv2.FastFeatureDetector_create()

# Detect keypoints
keypoints = fast.detect(img, None)

# Draw keypoints
img_fast = cv2.drawKeypoints(img, keypoints, None, color=(255,0,0))

# Show result
cv2.imshow('FAST Features', img_fast)
cv2.waitKey(0)
cv2.destroyAllWindows()
