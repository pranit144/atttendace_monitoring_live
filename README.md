# Classroom People Counter

This project is a Streamlit-based web application that uses OpenCV and Haar cascades to detect and count the number of people in a classroom from an uploaded image. It highlights detected faces by drawing bounding boxes around them.

## Features
- Upload an image in JPG, JPEG, or PNG format.
- Automatically detects and counts faces using Haar cascade detection.
- Displays the uploaded image with detected faces marked by bounding boxes.
- Outputs the total count of people detected in the image.

## Requirements
To run this project, you need the following:

- Python 3.7 or later
- Streamlit
- OpenCV
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/classroom-people-counter.git
   cd classroom-people-counter
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image file and see the detected faces and count.

## File Structure
- `app.py`: The main application script.
- `requirements.txt`: List of Python dependencies.

## How It Works

1. The user uploads an image through the Streamlit interface.
2. The image is processed using OpenCV to detect faces with a pre-trained Haar cascade classifier.
3. Detected faces are highlighted with bounding boxes.
4. The count of detected faces is displayed alongside the annotated image.

## Example Output

When an image is uploaded, the app displays the following:
- The uploaded image with bounding boxes drawn around detected faces.
- A success message showing the total count of detected people.

## Dependencies
Add the following dependencies to your `requirements.txt`:
```
streamlit
opencv-python
numpy
