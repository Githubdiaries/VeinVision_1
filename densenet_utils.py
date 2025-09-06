import numpy as np
import cv2

def preprocess_image(image, size=(224, 224)):
    """Preprocesses image for DenseNet input"""
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=size, mean=(104, 117, 123), swapRB=True, crop=False)
    return blob

def visualize_veins(original, mask, alpha=0.6):
    """Overlay mask on original image for visualization"""
    colored_mask = cv2.applyColorMap(mask, cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(original, 1 - alpha, colored_mask, alpha, 0)
    return overlay