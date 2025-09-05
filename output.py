import cv2
import numpy as np

# Pairs (original, processed) from captures folder
pairs = [
    ("captures/original_14.png", "captures/veins_14.png"),
    ("captures/original_18.png", "captures/veins_18.png"),
    ("captures/original_19.png", "captures/veins_19.png"),
]

rows = []

for orig, vein in pairs:
    img1 = cv2.imread(orig)
    img2 = cv2.imread(vein)

    if img1 is None or img2 is None:
        print(f"⚠️ Skipping {orig} or {vein}, file not found")
        continue

    # Resize processed to match original
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Combine each pair side by side
    combined_pair = cv2.hconcat([img1, img2])
    rows.append(combined_pair)

# Stack all pairs vertically
if rows:
    final_output = cv2.vconcat(rows)
    cv2.imwrite("captures/all_combined.png", final_output)
    print("✅ Saved captures/all_combined.png with 14,18,19 original+veins")
else:
    print("❌ No valid pairs found")
