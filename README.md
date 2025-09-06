<<<<<<< HEAD

## VeinVision_1

VeinVision_1 is a Python-based project that utilizes OpenCV to detect and visualize veins in hand images. It offers both static image processing and live video capture modes, providing flexibility for various use cases.

## 📂 Project Structure
VeinVision_1/

├── compare.py                                               # Script to generate side-by-side comparisons

├── live.py                                                # Live video capture and vein detection

├── static.py                                              # Static image processing for vein detection

├── static_input.png                                       # Sample input image for static processing

├── static_output.png                                      # Output image showing detected veins

├── captures/                                              # Folder for saving captured images (created during live capture)

└── README.md                                              # Project documentation


## 🖼 Static Image Processing

The static.py script processes a single input image (static_input.png) to detect veins and saves the output as static_output.png. This mode is suitable for testing and demonstrations without requiring a camera.


 *Usage* :

-> Place your input image in the repository directory and rename it to static_input.png.

-> Run the script:

  **python static.py**


-> The output will be saved as static_output.png.


## 🎥 Live Video Capture

The live.py script captures live video from a webcam or IP camera, processes each frame to detect veins, and displays the original and processed images side by side. It also allows manual capture of images during the live session.

 *Features* :

* Manual Capture: Press s to save the current frame and its processed version.

* Auto Capture: Press 1 to start auto-capturing frames for 20 seconds.

* Quit: Press q to exit the live capture.

## Requirements

1. Python 3.x

2. OpenCV (opencv-python)


## Usage

1. Ensure your camera is connected and accessible.

2. Run the script:

   **python live.py**


3. Follow the on-screen instructions for capturing images.

4. Captured images will be saved in the captures/ folder.



## Examples

### 1. Static Image Processing
Input image:

<img width="640" height="1280" alt="static_input (1)" src="https://github.com/user-attachments/assets/f7493a3b-9994-41f4-99c7-6d4ad3b0281b" />

Vein-detected output:

![Output Example](static_output.png)

---

### 2. Live Capture
Run the live script (`live/live.py`) to capture video from your phone camera or webcam.  

Press `1` to start auto-capture for 20 seconds, or `s` for manual capture.  

Captured images are saved in the `capture/` folder.

During live capture, the left side of the window displays the processed image (veins highlighted), and the right side shows the original frame.


Example of combined original vs detected veins:

<img width="1280" height="1440" alt="outputs" src="https://github.com/user-attachments/assets/cdf1f9d7-a333-4cf4-afe1-d384a1668afc" />











## 📌 Notes

The captures/ folder is created automatically during live capture to store images.

Ensure that your camera is properly configured and accessible by OpenCV for live capture functionality.












=======
# Vein Detection Using Computer Vision

A Python project to **detect veins in a hand image** using OpenCV and image processing techniques. The repository demonstrates step-by-step processing, from input to edge-detected veins.

---

##  Features

1. Converts the input image to **grayscale**.  
2. Extracts the **green channel** for better vein visibility.  
3. Applies **CLAHE (Contrast Limited Adaptive Histogram Equalization)** for contrast enhancement.  
4. Uses **Gaussian blur** to reduce noise.  
5. Performs **Canny edge detection** to highlight veins.  
6. Displays all intermediate steps for visualization and debugging.

---

##  Requirements

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  
- Matplotlib  

Install dependencies:

```bash
pip install opencv-python numpy matplotlib
```

##  Usage

1. Place your hand image in the repository folder and name it hand.jpg.

2. Run the script:

   python trial.py


3. The script displays 5 images:
   

**1) Original image

**2) Grayscale image

**3) Green channel extraction

**4) CLAHE + Gaussian blur result

**5) Final edge-detected veins

  ## Example

  Input image:

![Hand Input](static_input.png)


   Output (vein detection): ![Vein Detection Result](static_output.png)













>>>>>>> 55ea1d7 (Keep only 3 Python files in captures)
