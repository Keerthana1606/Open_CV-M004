import cv2
import numpy as np

# Create blank canvas
img = np.ones((500, 500, 3), dtype="uint8") * 255

drawing = False

# Mouse callback function
def draw(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", draw)

while True:
    cv2.imshow("Canvas", img)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()