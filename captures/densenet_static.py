import cv2
import numpy as np
import os
from densenet_utils import preprocess_image, visualize_veins

MODEL_PATH = "model/DenseNet_121.caffemodel"
PROTOTXT_PATH = "model/DenseNet_121.prototxt"
IMAGE_PATH = "static_input.png"
OUTPUT_PATH = "outputs/static_output.png"

def main():
    image = cv2.imread(IMAGE_PATH)
    if image is None:
        raise FileNotFoundError("static_input.png not found!")
    
    net = cv2.dnn.readNetFromCaffe(PROTOTXT_PATH, MODEL_PATH)
    blob = preprocess_image(image)
    net.setInput(blob)
    output = net.forward()
    
    # Assuming 'output' returns a segmentation mask.
    # For illustrative purposes: convert output to mask (see your model's specifics).
    mask = cv2.normalize(output[0,0,:,:], None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    result = visualize_veins(image, mask)
    cv2.imwrite(OUTPUT_PATH, result)
    print(f"Saved result as {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
