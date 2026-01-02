from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def vein_enhance(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    output_path = os.path.join(UPLOAD_FOLDER, "output.jpg")
    cv2.imwrite(output_path, enhanced)
    return output_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        input_path = os.path.join(UPLOAD_FOLDER, "input.jpg")
        file.save(input_path)

        vein_enhance(input_path)
        return render_template("index.html", result=True)

    return render_template("index.html", result=False)

app.run(host="0.0.0.0", port=81)
