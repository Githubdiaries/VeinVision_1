import cv2
import numpy as np
import os
from densenet_utils import preprocess_image, visualize_veins

MODEL_PATH = "model/DenseNet_121.caffemodel"
PROTOTXT_PATH = "model/DenseNet_121.prototxt"
OUTPUT_DIR = "outputs"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    net = cv2.dnn.readNetFromCaffe(PROTOTXT_PATH, MODEL_PATH)
    cap = cv2.VideoCapture(0)
    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        blob = preprocess_image(frame)
        net.setInput(blob)
        output = net.forward()
        
        mask = cv2.normalize(output[0,0,:,:], None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        overlay = visualize_veins(frame, mask)
        
        cv2.imshow('DenseNet Vein Detection (Press s to save, q to quit)', overlay)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'):
            fname = os.path.join(OUTPUT_DIR, f"live_output_{idx}.png")
            cv2.imwrite(fname, overlay)
            idx += 1
        elif key & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()