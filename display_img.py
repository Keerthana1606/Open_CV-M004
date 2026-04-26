import cv2

# Read the image
img = cv2.imread("C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/lib/site-packages/pet.jpg")  # replace with your image name or path

# Check if image loaded
if img is None:
    print("Error: Image not found!")
else:
    # Display the image
    cv2.imshow("Image", img)

    # Wait for key press
    cv2.waitKey(0)

    # Close window
    cv2.destroyAllWindows()