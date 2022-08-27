import cv2

video = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not video.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Posture Tracker', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

video.release()
cv2.destroyAllWindows()