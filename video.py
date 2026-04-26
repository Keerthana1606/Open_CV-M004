import cv2

# Load video file
cap = cv2.VideoCapture("C:/Users/B.Keerthana/PycharmProjects/OpenCV/.venv/VIRAT_S_050201_05_000890_000944.mp4")  # replace with your video file name

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

# Read and display video
while True:
    ret, frame = cap.read()

    # If no frame (end of video)
    if not ret:
        print("End of video")
        break

    # Show frame
    cv2.imshow("Video", frame)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()