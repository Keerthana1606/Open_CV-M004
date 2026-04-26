import cv2
import os
import numpy as np

# 📁 Path to dataset folder (change this)
input_folder = "frames"
output_folder = "output"

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Loop through all images in dataset
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # Read image
    img = cv2.imread(file_path)

    if img is None:
        print(f"Skipping {filename} (not an image)")
        continue

    # 1️⃣ Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2️⃣ Apply thresholding (binary image)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 3️⃣ Morphological operations

    # Erosion
    erosion = cv2.erode(binary, kernel, iterations=1)

    # Dilation
    dilation = cv2.dilate(binary, kernel, iterations=1)

    # Opening (Erosion → Dilation)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    # Closing (Dilation → Erosion)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Gradient (Difference between dilation and erosion)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    # 📁 Save results
    name = os.path.splitext(filename)[0]

    cv2.imwrite(os.path.join(output_folder, name + "_gray.jpg"), gray)
    cv2.imwrite(os.path.join(output_folder, name + "_binary.jpg"), binary)
    cv2.imwrite(os.path.join(output_folder, name + "_erosion.jpg"), erosion)
    cv2.imwrite(os.path.join(output_folder, name + "_dilation.jpg"), dilation)
    cv2.imwrite(os.path.join(output_folder, name + "_opening.jpg"), opening)
    cv2.imwrite(os.path.join(output_folder, name + "_closing.jpg"), closing)
    cv2.imwrite(os.path.join(output_folder, name + "_gradient.jpg"), gradient)

    print(f"Processed: {filename}")

print("✅ All images processed successfully!")