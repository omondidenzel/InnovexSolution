from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
import numpy as np
import PIL

app = Flask(__name__)

# Upload folder for classified images can be stored in some db in the future
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained model
MODEL_PATH = 'model/model.h5'
model = load_model(MODEL_PATH)

# Define class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Ensures upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def intro():
    """Introduction page."""
    return render_template('intro.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Image upload and classification page."""
    if request.method == 'POST':
        # Checker for if a file is uploaded
        if 'file' not in request.files:
            return "No file uploaded", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400
        
        # Saves the uploaded file in the system
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Image preprocessing for model input
        image = load_img(filepath, target_size=(32, 32))
        image_array = img_to_array(image) / 255.0       
        image_array = np.expand_dims(image_array, axis=0) 

        # Use the model to make a prediction
        predictions = model.predict(image_array)
        predicted_class = class_names[np.argmax(predictions)]

        return render_template('result.html', filename=file.filename, prediction=predicted_class)

    return render_template('index.html') 

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files."""
    return redirect(url_for('static', filename=f'uploads/{filename}'))

if __name__ == '__main__':
    app.run(debug=True)
