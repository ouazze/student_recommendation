from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import json
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the model, scaler, and label mapping
model = load_model("student_recommendation_model.keras")
scaler = joblib.load("scaler.pkl")

with open("label_mapping.json", "r") as f:
    label_mapping = json.load(f)

# Define features
features = [
    'Arabic', 'English', 'French', 'Mathematics', 'Science',
    'Religious Studies', 'Computer Science', 'Philosophy', 'Art', 'Social Studies'
]

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Retrieve user inputs
            user_input = [float(request.form[feature]) for feature in features]
            
            # Normalize the input data
            user_data_scaled = scaler.transform([user_input])
            
            # Predict recommendation
            prediction = model.predict(user_data_scaled)
            predicted_class = prediction.argmax(axis=1)[0]
            
            # Retrieve the recommendation
            recommendation = label_mapping[str(predicted_class)]

            return render_template("result.html", recommendation=recommendation)
        except Exception as e:
            return jsonify({"error": str(e)})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
