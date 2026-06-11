# 📱 AI-Powered Mobile Phone Usage Detection System

A real-time computer vision application built using YOLOv8, OpenCV, and Python that detects mobile phone usage from a live webcam feed.

The system identifies people and mobile phones, highlights potential phone usage events, logs violations, captures screenshots, and provides real-time monitoring statistics.

---

## 🚀 Features

* Real-time object detection using YOLOv8
* Mobile phone usage monitoring
* Live webcam integration
* Confidence score display
* Violation detection and tracking
* Automatic screenshot capture
* CSV-based violation logging
* FPS (Frames Per Second) monitoring
* Timestamped surveillance records
* OpenCV-powered visualization

---

## 🛠️ Tech Stack

* Python
* YOLOv8
* OpenCV
* Ultralytics
* NumPy

---

## 📂 Project Structure

AI-Mobile-Phone-Usage-Detector/

├── detect.py

├── requirements.txt

├── README.md

├── .gitignore

├── violations/

└── violations_log.csv

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Mobile-Phone-Usage-Detector.git
cd AI-Mobile-Phone-Usage-Detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python detect.py
```

---

## 🎯 How It Works

1. Captures live video from the webcam.
2. Uses YOLOv8 to detect people and mobile phones.
3. Checks whether a phone is associated with a detected person.
4. Displays a warning banner for potential phone usage.
5. Saves screenshots of violations.
6. Logs events with timestamps into a CSV file.

---
## 📸 Demo

<img width="640" height="480" alt="violation_2026-06-11_16-29-31" src="https://github.com/user-attachments/assets/847b6cb9-1842-4ab3-a8e2-1e54e554a2db" />


## 📸 Sample Output

* Person Detection
* Mobile Phone Detection
* Real-Time Bounding Boxes
* Confidence Scores
* Violation Alerts
* FPS Monitoring

---

## 🔮 Future Enhancements

* Multi-object tracking
* Streamlit web dashboard
* Email notifications
* Cloud-based monitoring
* Custom-trained detection models
* Smart classroom analytics

---

## 👨‍💻 Author

Akshith Avunuri

Computer Science Student | AIML Enthusiast | Full Stack Developer

---

⭐ If you found this project useful, consider giving it a star.
