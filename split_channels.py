import cv2

# Read image
img = cv2.imread("pet.jpg")

# Split channels (B, G, R)
b, g, r = cv2.split(img)

# Show channels
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

# Merge channels back
merged = cv2.merge((b, g, r))

cv2.imshow("Merged Image", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()