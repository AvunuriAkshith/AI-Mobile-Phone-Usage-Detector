from ultralytics import YOLO
import cv2
import time
import csv
import os
from datetime import datetime

# ==========================
# LOAD YOLO MODEL
# ==========================
model = YOLO("yolov8n.pt")

# ==========================
# CREATE FOLDERS
# ==========================
os.makedirs("violations", exist_ok=True)

# ==========================
# CSV LOG FILE
# ==========================
csv_file = "violations_log.csv"

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Event"])

# ==========================
# SETTINGS
# ==========================
ALERT_INTERVAL = 5  # seconds

last_alert_time = 0
violation_count = 0

# ==========================
# SAVE VIOLATION
# ==========================
def save_violation(frame):
    global violation_count

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    image_path = f"violations/violation_{timestamp}.jpg"

    cv2.imwrite(image_path, frame)

    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Mobile Phone Usage Detected"
        ])

    violation_count += 1

# ==========================
# WEBCAM
# ==========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not found!")
    exit()

print("Press Q to quit")

# FPS Calculation
prev_time = time.time()

# ==========================
# MAIN LOOP
# ==========================
while True:

    success, frame = cap.read()

    if not success:
        break

    # YOLO Detection
    results = model(frame, verbose=False)

    persons = []
    phones = []

    # ------------------------
    # Process Detections
    # ------------------------
    for r in results:

        for box in r.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            conf = float(box.conf[0])
            cls = int(box.cls[0])

            label = model.names[cls]

            if label == "person":
                persons.append((x1, y1, x2, y2))

            elif label == "cell phone":
                phones.append((x1, y1, x2, y2))

            # Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Label + Confidence
            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

    # ------------------------
    # Phone Usage Detection
    # ------------------------
    phone_usage_detected = False

    for px1, py1, px2, py2 in persons:

        for fx1, fy1, fx2, fy2 in phones:

            center_x = (fx1 + fx2) // 2
            center_y = (fy1 + fy2) // 2

            if (px1 <= center_x <= px2 and
                    py1 <= center_y <= py2):

                phone_usage_detected = True

                cv2.rectangle(
                    frame,
                    (px1, py1),
                    (px2, py2),
                    (0, 0, 255),
                    3
                )

    # ------------------------
    # Alert Banner
    # ------------------------
    if phone_usage_detected:

        cv2.rectangle(
            frame,
            (10, 10),
            (650, 70),
            (0, 0, 255),
            -1
        )

        cv2.putText(
            frame,
            "MOBILE PHONE USAGE DETECTED",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2
        )

        current_time = time.time()

        if current_time - last_alert_time > ALERT_INTERVAL:

            save_violation(frame)

            last_alert_time = current_time

    # ------------------------
    # FPS Counter
    # ------------------------
    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    # ------------------------
    # Violation Counter
    # ------------------------
    cv2.putText(
        frame,
        f"Violations: {violation_count}",
        (20, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    # ------------------------
    # Timestamp
    # ------------------------
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cv2.putText(
        frame,
        timestamp,
        (20, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # ------------------------
    # Display
    # ------------------------
    cv2.imshow(
        "AI Mobile Phone Usage Detection System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==========================
# CLEANUP
# ==========================
cap.release()
cv2.destroyAllWindows()