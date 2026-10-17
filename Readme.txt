VeinVision
==========

PROJECT OVERVIEW
----------------

VeinVision is a handheld vein-visualisation project exploring near-infrared (NIR) imaging, computer vision, and visible-light projection.

The current hardware platform is a Raspberry Pi 4B (2 GB RAM) with an IMX219 NoIR camera and an 850 nm infrared LED array.

The intended system will capture NIR images, process them using OpenCV, and deliver camera video to a laptop browser over HTTP. HLS is the planned video delivery method, with Tailscale providing private remote access.


HARDWARE
--------

- Raspberry Pi 4B, 2 GB RAM
- IMX219 NoIR camera module
- 850 nm infrared LED array
- 64 GB microSD card
- Compatible Raspberry Pi power supply
- MicroSD card reader required for flashing


SOFTWARE AND SETUP
------------------

- Raspberry Pi Imager installed on Windows
- Tailscale installed on Windows
- Windows OpenSSH client available for terminal-based access
- Raspberry Pi OS Lite (64-bit) selected for the planned headless setup
- SSH, camera access, OpenCV processing, and HTTP/HLS streaming remain to be verified on the Raspberry Pi


WINDOWS CHECKS
==============

File: windows_checks.ps1

ssh -V
tailscale status
tailscale ip -4


CAMERA CHECKS
=============

File: camera_check.sh

rpicam-hello --list-cameras
rpicam-still --nopreview --timeout 2000 --output test.jpg


PYTHON AND OPENCV CHECKS
========================

File: opencv_check.sh

python3 -c "from picamera2 import Picamera2; print('Picamera2 OK')"
python3 -c "import cv2; print(cv2.__version__)"


HTTP AND HLS SERVER CHECKS
==========================

File: http_hls_check.sh

sudo systemctl status mediamtx --no-pager
curl -f http://127.0.0.1:8888/cam/index.m3u8 | head
sudo tailscale serve status


PLANNED ARCHITECTURE
====================

Camera:
IMX219 NoIR

NIR Illumination:
850 nm infrared LED array

Processing:
Python and OpenCV on Raspberry Pi

Video Delivery:
H.264 video through MediaMTX using HLS over HTTP

Remote Access:
Tailscale

Client:
Laptop web browser

Future Direction:
Vein enhancement, optical alignment, and visible-light vein projection.


CURRENT STATUS
==============

Completed:
- Hardware components identified for the initial prototype
- Hardware and software architecture planned
- Raspberry Pi Imager installed on Windows
- Tailscale installed on Windows
- 64 GB microSD card available

Pending Verification:
- Raspberry Pi OS flashing and first boot
- SSH connection to the Raspberry Pi
- Tailscale connection between the laptop and Raspberry Pi
- IMX219 camera detection and image capture
- Python and OpenCV availability on the Raspberry Pi
- MediaMTX installation and HLS video delivery
- Browser access to the live camera feed
- Vein enhancement and projector integration


NOTE
====

The commands above are verification commands for their respective setup stages. They do not indicate that the Raspberry Pi camera, remote connection, or video server has already been tested successfully.