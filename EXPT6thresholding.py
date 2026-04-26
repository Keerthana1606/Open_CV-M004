import cv2

# 1. Read image in grayscale
img = cv2.imread("C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/Lib/site-packages/Bear.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found")
    exit()

# 2. Apply Thresholding Methods

# (a) Simple Binary Threshold
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# (b) Adaptive Mean Threshold
adaptive_mean = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

# (c) Adaptive Gaussian Threshold
adaptive_gaussian = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

# (d) Otsu Threshold
ret2, otsu = cv2.threshold(
    img, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# 3. Display Images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Threshold", binary)
cv2.imshow("Adaptive Mean", adaptive_mean)
cv2.imshow("Adaptive Gaussian", adaptive_gaussian)
cv2.imshow("Otsu Threshold", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Segmentation Analysis (using Otsu result)

print("Otsu Threshold Value:", ret2)

white_pixels = cv2.countNonZero(otsu)
total_pixels = img.size
black_pixels = total_pixels - white_pixels

print("White Pixels (Foreground):", white_pixels)
print("Black Pixels (Background):", black_pixels)

print("Foreground Percentage:", (white_pixels / total_pixels) * 100)
print("Background Percentage:", (black_pixels / total_pixels) * 100)
