# Image Classification Using TensorFlow

## Overview

The goal of this project is to classify images into their correct categories using TensorFlow libraries. The dataset used in this project contains 10 categories of images. Flask has been used to deploy this project, providing users with a UI to upload and classify their images.

### Features

- **Dataset**: [CIFAR-10 Dataset](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data)
  - Total images: 60,000
  - Training (50,000) and test images (10,000)
  - Image size: 32*32
- **Image Classification**: Classifies images into 10 predefined categories.
- **Web Interface**: Flask-based UI for user interaction.

## Setup Instructions

Follow the steps below to set up the project on your local machine:

### Prerequisites

- [Python 3.12](https://www.python.org/downloads/)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd projectinnovex
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment:
   - Create a virtual environment:
     ```bash
     virtualenv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

### Running the Project

1. Start the Flask application:
   ```bash
   python3 app.py
   ```

2. Access the application at `http://localhost:5000`.


