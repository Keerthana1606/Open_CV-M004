import cv2

img = cv2.imread("Food delivery.png")

# alpha = contrast (1.0-3.0), beta = brightness (0-100)
alpha = 1.5   # Contrast control
beta = 50     # Brightness control

adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

cv2.imshow("Brightness & Contrast Adjusted", adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
