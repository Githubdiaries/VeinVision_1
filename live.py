import cv2
import numpy as np
import time
import os

# Replace with your IP Webcam URL or 0 for webcam
video_source = "http://192.168.1.6:4747/video"
# video_source = 0

cap = cv2.VideoCapture(video_source)

# Create folder to save captured images
os.makedirs("captures", exist_ok=True)

def process_frame(frame):
    """Highlight veins in the frame"""
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Green channel extraction for vein contrast
    green = frame[:, :, 1]
    
    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(green)
    
    # Blur to reduce noise
    blur = cv2.GaussianBlur(enhanced, (5,5), 0)
    
    # Edge detection
    edges = cv2.Canny(blur, 50, 150)
    
    return edges

auto_capturing = False
auto_start_time = None
capture_interval = 0.5  # seconds between auto captures
last_capture_time = 0
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    veins = process_frame(frame)
    combined = cv2.hconcat([cv2.cvtColor(veins, cv2.COLOR_GRAY2BGR), frame])
    cv2.imshow("VeinVision Live (Left=Veins, Right=Original)", combined)
    
    key = cv2.waitKey(1) & 0xFF

    # Manual capture
    if key == ord('s'):
        frame_count += 1
        cv2.imwrite(f"captures/original_{frame_count}.png", frame)
        cv2.imwrite(f"captures/veins_{frame_count}.png", veins)
        print(f"Manual capture saved: original_{frame_count}, veins_{frame_count}")

    # Start auto capture
    if key == ord('1') and not auto_capturing:
        auto_capturing = True
        auto_start_time = time.time()
        last_capture_time = 0
        print("Started auto-capture for 20 seconds...")

    # Handle auto capturing
    if auto_capturing:
        elapsed = time.time() - auto_start_time
        if elapsed <= 20:
            if time.time() - last_capture_time >= capture_interval:
                frame_count += 1
                cv2.imwrite(f"captures/original_{frame_count}.png", frame)
                cv2.imwrite(f"captures/veins_{frame_count}.png", veins)
                print(f"Auto-capture saved: original_{frame_count}, veins_{frame_count}")
                last_capture_time = time.time()
        else:
            auto_capturing = False
            print("Auto-capture finished.")

    # Quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Save captured images in 'captures' folder
