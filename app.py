from flask import Flask, request, render_template, redirect, url_for
import os
import numpy as np
import tensorflow as tf
from PIL import Image

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the trained model
model = tf.keras.models.load_model("lung_cancer_cnn_model.h5")

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path).convert("L")  # Convert to grayscale
    image = image.resize((28, 28))              # Resize to 28x28
    image_array = np.array(image) / 255.0       # Normalize pixel values
    return image_array.reshape(1, 28, 28, 1)    # Reshape for model input

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            # Preprocess and predict
            processed_image = preprocess_image(file_path)
            prediction = model.predict(processed_image)
            result = "Cancer Detected" if prediction[0][0] > 0.5 else "No Cancer Detected"
            
            # Render the result page
            return render_template('result.html', result=result, image_path=file_path)
    return render_template('index.html', result=None)



if __name__ == '__main__':
    app.run(debug=True)
