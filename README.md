# Vein Detection Using Computer Vision

A Python project to **detect veins in a hand image** using OpenCV and image processing techniques. The repository demonstrates step-by-step processing, from input to edge-detected veins.

---

## 1. Features

1. Converts the input image to **grayscale**.  
2. Extracts the **green channel** for better vein visibility.  
3. Applies **CLAHE (Contrast Limited Adaptive Histogram Equalization)** for contrast enhancement.  
4. Uses **Gaussian blur** to reduce noise.  
5. Performs **Canny edge detection** to highlight veins.  
6. Displays all intermediate steps for visualization and debugging.

---

## 2. Requirements

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  
- Matplotlib  

Install dependencies:

```bash
pip install opencv-python numpy matplotlib
