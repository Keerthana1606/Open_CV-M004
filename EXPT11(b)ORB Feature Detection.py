import cv2

# Read image
img = cv2.imread('pet.jpg', 0)

# Create ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
keypoints, descriptors = orb.detectAndCompute(img, None)

# Draw keypoints
img_kp = cv2.drawKeypoints(img, keypoints, None, color=(0,255,0))

# Show result
cv2.imshow('ORB Features', img_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()
