import cv2
import matplotlib.pyplot as plt

# 1. Read the input image
img = cv2.imread("Food delivery.png")   # change path if needed

if img is None:
    print("Error: Image not found")
    exit()

# Convert BGR to RGB (for correct display in matplotlib)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. Convert to grayscale (Single intensity channel)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Histogram Equalization
equalized = cv2.equalizeHist(gray)

# 4. Histogram Stretching (Normalization)
normalized = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

# 5. Plot Histograms for B, G, R channels
colors = ('b', 'g', 'r')
plt.figure(figsize=(10, 5))
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
plt.title("Histogram for B, G, R Channels")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

# 6. Display all images
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(equalized, cmap='gray')
plt.title("Histogram Equalization")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(normalized, cmap='gray')
plt.title("Histogram Stretching")
plt.axis('off')

plt.show()