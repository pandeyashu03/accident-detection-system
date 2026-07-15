# 🚗 Accident Detection System using Deep Learning and OpenCV

A real-time Accident Detection System that detects road accidents from CCTV footage, webcam streams, or recorded videos using Deep Learning and Computer Vision. The system automatically sends an **email alert** whenever an accident is detected, making it suitable for intelligent traffic monitoring and emergency response applications.

<p align="center">
  <img src="Demo.gif" alt="Project Demo" width="800"/>
</p>

---

## 📌 Overview

Road accidents are one of the leading causes of injuries and fatalities worldwide. Delays in identifying accidents often lead to slower emergency response.

This project uses a Convolutional Neural Network (CNN) trained on accident images to classify video frames in real time. When an accident is detected with high confidence, the system immediately sends an email notification to a predefined recipient.

---

## ✨ Features

- 🚗 Real-time accident detection from live camera or recorded videos
- 🧠 CNN-based accident classification model
- 🎥 Supports webcam and CCTV footage
- 📧 Automatic email alert system upon accident detection
- 📊 Displays prediction confidence in real time
- ⚡ Modular Python implementation
- 🔄 Easy to customize and extend

---

## 🛠️ Tech Stack

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- SMTP (Email Alerts)

---

## 📂 Project Structure

```text
Accident-Detection-System/
│
├── main.py
├── detection.py
├── camera.py
├── alert.py
├── check.py
├── accident-classification.ipynb
├── model.json
├── model_weights.h5
├── requirements.txt
├── README.md
└── Demo.gif
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/accident-detection-system.git
```

### 2. Navigate to the project directory

```bash
cd accident-detection-system
```

### 3. Create a virtual environment (Recommended)

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the application using:

```bash
python main.py
```

The application will:

- Access the camera or video stream
- Analyze each frame using the trained CNN model
- Detect possible accidents
- Trigger an automatic email notification if an accident is detected

---

## 📧 Email Alert System

One of the key enhancements in this project is the **automatic email alert feature**.

Whenever the system detects an accident with high confidence, it automatically sends an email notification to a configured recipient. This demonstrates how AI-based accident detection can be integrated with real-world notification systems for faster emergency response.

---

## 🧠 Model

The deep learning model is trained using accident image data and exported as:

- `model.json`
- `model_weights.h5`

These files are loaded during inference to classify incoming video frames.

---

## 📸 Demo

The repository includes a demonstration GIF showing the system detecting accidents in real time.

<p align="center">
  <img src="Demo.gif" width="800">
</p>

---

## 🚀 Future Improvements

- 📍 GPS location sharing
- 📱 SMS notification integration
- ☎ Emergency service notification
- 🌐 Cloud deployment
- 🚦 Multiple camera support
- 🤖 Higher accuracy using advanced object detection models such as YOLOv8

---

## 🤝 Acknowledgements

This project builds upon publicly available research and open-source ideas in accident detection using deep learning. Additional enhancements, including the automatic email alert system, project refinements, and documentation improvements, have been incorporated as part of this implementation.

---

## 👨‍💻 Author

**Ashutosh Kumar Pandey**

- GitHub: https://github.com/pandeyashu03

---

## ⭐ If you found this project useful, consider giving it a star.