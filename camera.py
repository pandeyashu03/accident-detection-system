import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
from alert import send_email_alert, play_alert, show_popup  # ✅ NEW

model = AccidentDetectionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

def startapplication(video_path="C:/Users/wwwas/Downloads/Accident demo.gif"):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"[ERROR] Cannot open video source: {video_path}")
        return

    while True:
        ret, frame = video.read()

        if not ret or frame is None:
            print("[INFO] End of video or cannot read frame.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])

        if pred == "Accident":
            prob = round(prob[0][0] * 100, 2)
            cv2.rectangle(frame, (0, 0), (350, 50), (0, 0, 0), -1)
            cv2.putText(frame, f"{pred}: {prob}%", (20, 35), font, 1, (255, 255, 0), 2)

            # ✅ NEW — Alert System
            if prob > 90:
                play_alert()
                send_email_alert()
                show_popup()

        cv2.imshow("Accident Detection System", frame)

        if cv2.waitKey(33) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()