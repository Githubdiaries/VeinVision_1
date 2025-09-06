import cv2
import numpy as np
import time
import os 
from datetime import datetime

# Replace with your IP Webcam URL or 0 for webcam
video_source = "http://192.168.1.6:4747/video"
# video_source = 0

cap = cv2.VideoCapture(video_source)

# Create folder to save captured images
os.makedirs("captures", exist_ok=True)

# Parameters (tweak as needed)
CLAHE_CLIP_LIMIT = 2.0
CLAHE_TILE_GRID_SIZE = (8, 8)
CANNY_THRESHOLD1 = 50
CANNY_THRESHOLD2 = 150
AUTO_CAPTURE_DURATION = 20  # seconds
CAPTURE_INTERVAL = 0.5     # seconds between auto captures

def process_frame(frame):
    """Highlight veins in the frame using CLAHE and Canny Edge Detection"""
    # Green channel extraction for better vein contrast
    green = frame[:, :, 1]

    # Enhance contrast with CLAHE
    clahe = cv2.createCLAHE(clipLimit=CLAHE_CLIP_LIMIT, tileGridSize=CLAHE_TILE_GRID_SIZE)
    enhanced = clahe.apply(green)

    # Blur to reduce noise
    blur = cv2.GaussianBlur(enhanced, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blur, CANNY_THRESHOLD1, CANNY_THRESHOLD2)

    return edges

def save_capture(frame, veins):
    """Save original, edges, and overlay images with timestamp filenames"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    orig_filename = f"captures/original_{timestamp}.png"
    veins_filename = f"captures/veins_{timestamp}.png"
    overlay_filename = f"captures/overlay_{timestamp}.png"

    cv2.imwrite(orig_filename, frame)
    cv2.imwrite(veins_filename, veins)

    # Create color overlay of veins on original image
    veins_colored = cv2.applyColorMap(veins, cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(frame, 0.7, veins_colored, 0.3, 0)
    cv2.imwrite(overlay_filename, overlay)
    print(f"Saved captures: {orig_filename}, {veins_filename}, {overlay_filename}")

auto_capturing = False
auto_start_time = None
last_capture_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame capture failed, retrying in 0.5s...")
        time.sleep(0.5)
        cap.release()
        cap = cv2.VideoCapture(video_source)
        continue

    veins = process_frame(frame)
    combined = cv2.hconcat([cv2.cvtColor(veins, cv2.COLOR_GRAY2BGR), frame])
    cv2.imshow("VeinVision Live (Left=Veins, Right=Original)", combined)

    key = cv2.waitKey(1) & 0xFF

    # Manual capture with 's'
    if key == ord('s'):
        save_capture(frame, veins)

    # Start auto capture with '1'
    if key == ord('1') and not auto_capturing:
        auto_capturing = True
        auto_start_time = time.time()
        last_capture_time = 0
        print("Started auto-capture for 20 seconds...")

    # Handle auto capturing
    if auto_capturing:
        elapsed = time.time() - auto_start_time
        if elapsed <= AUTO_CAPTURE_DURATION:
            if time.time() - last_capture_time >= CAPTURE_INTERVAL:
                save_capture(frame, veins)
                last_capture_time = time.time()
        else:
            auto_capturing = False
            print("Auto-capture finished.")

    # Quit with 'q'
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
