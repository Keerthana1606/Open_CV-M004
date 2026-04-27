import cv2

# Read the image
img = cv2.imread('pet.jpg')

# Check if image loaded
if img is None:
    print("Error: Image not found")
else:
    # Shape (height, width, channels)
    print("Shape:", img.shape)

    # Size (total number of pixels)
    print("Size:", img.size)

    # Datatype (pixel type)
    print("Datatype:", img.dtype)
