from flask import Flask, render_template, request, url_for
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import json
import os

app = Flask(__name__)

# Folder to save uploads
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model and class indices
model = load_model("plant_disease_model.h5")
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

# Reverse mapping {0:"class1", 1:"class2", ...}
class_labels = {v: k for k, v in class_indices.items()}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return render_template("index.html", label="❌ No file uploaded")

    file = request.files["file"]
    if file.filename == "":
        return render_template("index.html", label="❌ No file selected")

    # Save uploaded file in static/uploads
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Preprocess image
    img = image.load_img(filepath, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = float(np.max(predictions)) * 100
    result_class = class_labels[predicted_class]

    # Generate image URL for template
    image_url = url_for("static", filename="uploads/" + file.filename)

    return render_template("index.html",
                           image_url=image_url,
                           label=result_class,
                           confidence=f"{confidence:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
