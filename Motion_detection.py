import cv2

# Load video
cap = cv2.VideoCapture('C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/VIRAT_S_050201_05_000890_000944.mp4')

# Check video
if not cap.isOpened():
    print("Error: Video not opening")
    exit()

# Read frames
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while ret1 and ret2:

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Difference
    diff = cv2.absdiff(gray1, gray2)

    # Threshold
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Dilate
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0), 2)

    # 🔥 IMPORTANT (this shows output)
    cv2.imshow("Motion Detection", frame1)
    cv2.imshow("Threshold", thresh)

    # Next frame
    frame1 = frame2
    ret2, frame2 = cap.read()

    # Exit key
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()