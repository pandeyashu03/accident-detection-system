import cv2

path = "C:/Users/wwwas/Downloads/Accident demo.gif"
cap = cv2.VideoCapture(path)
if not cap.isOpened():
    print("[ERROR] Cannot open video file:", path)
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("[INFO] End of video or unable to read frame.")
        break

    cv2.imshow("Test Video", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
