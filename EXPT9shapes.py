import cv2
import numpy as np

# 1. Read the input image
img = cv2.imread("C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/Lib/site-packages/triangle.png")   # Change path if needed
if img is None:
    print("Error: Image not found")
    exit()

# Resize (optional for better visibility)
img = cv2.resize(img, (600, 600))

# Create a copy for drawing
output = img.copy()

# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Apply Gaussian Blur (noise removal)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 4. Apply Thresholding
_, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)

# 5. Detect contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 6. Loop through contours
for cnt in contours:
    # Calculate area to ignore small noise
    area = cv2.contourArea(cnt)
    if area < 500:
        continue

    # 7. Approximate contour shape
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # Get number of vertices
    vertices = len(approx)

    # Get bounding box for label position
    x, y, w, h = cv2.boundingRect(approx)

    # 8. Identify shape
    if vertices == 3:
        shape = "Triangle"

    elif vertices == 4:
        # Check aspect ratio to differentiate square/rectangle
        aspect_ratio = w / float(h)
        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"

    elif vertices > 4:
        shape = "Circle"

    else:
        shape = "Unknown"

    # 9. Draw contour and label
    cv2.drawContours(output, [approx], -1, (0, 255, 0), 2)
    cv2.putText(output, shape, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# 10. Display output
cv2.imshow("Original Image", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Detected Shapes", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
