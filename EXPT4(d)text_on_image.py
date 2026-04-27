import cv2

img = cv2.imread("Bear.jpg")

# Add text (text, position, font, scale, color, thickness)
cv2.putText(img, "Hello OpenCV!", (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 0, 0), 2)

cv2.imshow("Text Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
