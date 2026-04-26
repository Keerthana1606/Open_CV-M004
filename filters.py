import cv2

# 1. Read the input image
img = cv2.imread("C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/Lib/site-packages/Bear.jpg")


if img is None:
    print(" Image not found. Check path!")
    exit()

# Safe now
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Optional: resize for display (so it fits screen)
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 2. Apply filters

# Averaging Filter (Blur)
avg = cv2.blur(img, (5, 5))

# Gaussian Filter
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Filter
median = cv2.medianBlur(img, 5)

# Bilateral Filter
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 3. Display all images
cv2.imshow("Original Image", img)
cv2.imshow("Averaging Filter", avg)
cv2.imshow("Gaussian Filter", gaussian)
cv2.imshow("Median Filter", median)
cv2.imshow("Bilateral Filter", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()