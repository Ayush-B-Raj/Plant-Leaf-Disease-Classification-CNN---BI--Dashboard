# 🌿 Plant Disease Image Classification + Power BI Dashboard  

**Authors**: Anjala Nishar, Ayush B Raj, Abhijith K Sajeev (Team Gamma)  
**Internship**: TechMaghi – Data Science Intern  
**Project Duration**: August 2025  

---

## 🧠 Project Overview  

This project focuses on **automated plant leaf disease classification** using a **Convolutional Neural Network (CNN)** built with **Keras/TensorFlow**. The trained model can classify different plant diseases from leaf images with high accuracy.  

The results are exported and visualized in a **Power BI dashboard**, enabling **agricultural advisors, researchers, and farmers** to interpret disease trends and make data-driven decisions.  

---

## ✨ Features  

- **Flask Web Application**  
  - Upload a leaf image.  
  - Get predicted **disease name** and **confidence score** instantly.  

- **Machine Learning Pipeline**  
  - Pretrained CNN model: `plant_disease_model.h5`  
  - Class label mappings: `class_indices.json`  
  - Evaluation metrics (precision, recall, F1, confusion matrix).  

- **Business Intelligence (BI) Dashboard**  
  - Interactive **Power BI dashboard** created using exported CSV metrics.  
  - Supports analysis of accuracy trends, per-class metrics, and prediction insights.  

---

## 🗂 Repository Structure  

```
project/
├── app.py                        # Flask inference server
├── plant_disease_model.h5        # Trained CNN model
├── class_indices.json            # Class → Index mapping
├── history.csv                   # Training/validation accuracy & loss per epoch
├── classification_metrics.csv    # Per-class precision, recall, F1, support
├── confusion_matrix.csv          # Confusion matrix results
├── predictions.csv               # Predictions for all test images
├── sample_predictions.csv        # Subset of predictions for dashboard
├── templates/                    # Flask HTML templates
│   └── index.html
├── uploads/                      # Uploaded images during runtime
├── requirements.txt              # Dependencies
└── dashboard.pbix                # Power BI report file
```

---

## 🚀 How to Run  

### 1. Create & Activate Virtual Environment  
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3. Start Flask Application  
```bash
# Option 1: Using Flask CLI
set FLASK_APP=app.py       # Windows
export FLASK_APP=app.py    # macOS/Linux
flask run

# Option 2: Using Python
python app.py
```

### 4. Access Web App  
Open: **http://127.0.0.1:5000/** in a browser.  
Upload a leaf image → get disease prediction + confidence.  

---

## 📊 Power BI Dashboard  

The exported CSV files (`history.csv`, `classification_metrics.csv`, `confusion_matrix.csv`, `predictions.csv`) can be directly imported into **Power BI Desktop**.  

Recommended visuals:  
- **Accuracy & Loss Trends** – Line chart using `history.csv`.  
- **Per-Class Metrics** – Bar/column chart using `classification_metrics.csv`.  
- **Confusion Matrix** – Heatmap using `confusion_matrix.csv`.  
- **Prediction Insights** – Table/gallery using `predictions.csv`.  

---

## 🔧 Troubleshooting  

- **Keras/TensorFlow version issues**:  
  - Ensure imports are from `tensorflow.keras`.  
  - Use pinned versions from `requirements.txt` (TensorFlow 2.15 + Keras 2.15).  

- **Model not found**: Keep `plant_disease_model.h5` and `class_indices.json` in the same directory as `app.py`.  

- **Template errors**: The Flask template (`index.html`) expects variables:  
  - `image_url` → path to uploaded image  
  - `label` → predicted disease  
  - `confidence` → prediction probability  

---

## 📎 Key Outputs  

- **Model Training History** – `history.csv`  
- **Evaluation Metrics** – `classification_metrics.csv`  
- **Confusion Matrix** – `confusion_matrix.csv`  
- **Predictions** – `predictions.csv`, `sample_predictions.csv`  

---

## 📬 Contact  

- **Anjala Nishar** – anjalanishar61@gmail.com  
- **Ayush B Raj** – ayushbraj999@gmail.com  
- **Abhijith K Sajeev** – abhijithksajeevkaliyath@gmail.com  
