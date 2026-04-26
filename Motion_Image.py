import cv2
import glob

# Load all images
images = sorted(glob.glob('frames/*.jpg'))

print("Images found:", images)   # 🔍 DEBUG

if len(images) < 2:
    print("Not enough images to detect motion")
    exit()

for i in range(len(images) - 1):
    print("Processing:", images[i], images[i+1])  # 🔍 DEBUG

    img1 = cv2.imread(images[i])
    img2 = cv2.imread(images[i+1])

    # Check image loading
    if img1 is None or img2 is None:
        print("Error loading images")
        continue

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Difference
    height, width = gray1.shape
    gray2 = cv2.resize(gray2, (width, height))
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
        cv2.rectangle(img1, (x,y), (x+w,y+h), (0,255,0), 2)

    # Show output
    cv2.imshow("Motion Detection", img1)
    cv2.imshow("Threshold", thresh)

    # 🔥 IMPORTANT (keep window open)
    key = cv2.waitKey(0)   # changed from 500 → 0
    if key == 27:
        break

cv2.destroyAllWindows()