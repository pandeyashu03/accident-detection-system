
from email.mime.text import MIMEText
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import os

# ─── Email Alert ───────────────────────────────────────────
def send_email_alert():
    sender = "your.email@gmail.com"
    receiver = "alert.receiver@gmail.com"
    password = "your_app_password"  # Gmail App Password

    time_of_accident = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = MIMEText(f"⚠️ Accident Detected at {time_of_accident}. Please take immediate action.")
    msg["Subject"] = "🚨 Accident Alert!"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

    print("Alert email sent!")

# ─── Sound Alert ───────────────────────────────────────────
def play_alert():
    # For Windows:
    import winsound
    winsound.Beep(1000, 2000)


# ─── Popup Alert ───────────────────────────────────────────
def show_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("🚨 Accident Detected!",
                           "An accident has been detected! Alerting authorities...")
    root.destroy()