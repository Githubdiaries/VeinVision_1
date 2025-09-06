import cv2
import os

# Folder containing images (relative to repo)
folder = "samples"

# Collect all original and vein files
files = os.listdir(folder)
originals = [f for f in files if f.startswith("original_")]
veins = [f for f in files if f.startswith("veins_")]

# Extract common indices (numbers)
orig_indices = {f.split("_")[1].split(".")[0] for f in originals}
vein_indices = {f.split("_")[1].split(".")[0] for f in veins}
common_indices = sorted(orig_indices & vein_indices, key=lambda x: int(x))

rows = []

for idx in common_indices:
    orig_path = os.path.join(folder, f"original_{idx}.png")
    vein_path = os.path.join(folder, f"veins_{idx}.png")

    img1 = cv2.imread(orig_path)
    img2 = cv2.imread(vein_path)

    if img1 is None or img2 is None:
        print(f"⚠️ Skipping {idx}, missing file")
        continue

    # Resize vein to match original
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Combine side by side
    combined = cv2.hconcat([img1, img2])
    rows.append(combined)

# Stack vertically
if rows:
    final_output = cv2.vconcat(rows)
    out_path = os.path.join(folder, "all_combined.png")
    cv2.imwrite(out_path, final_output)
    print(f"✅ Saved {out_path} with {len(rows)} pairs")
else:
    print("⚠️ No matching pairs found!")
