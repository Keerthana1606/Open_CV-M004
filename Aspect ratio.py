import cv2

# Read image
img = cv2.imread("Food delivery.png")

# Get original dimensions
h, w = img.shape[:2]

# Maintain aspect ratio (scale factor)
scale = 0.5
new_width = int(w * scale)
new_height = int(h * scale)

aspect_resized = cv2.resize(img, (new_width, new_height))

cv2.imshow("Aspect Ratio Maintained", aspect_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()