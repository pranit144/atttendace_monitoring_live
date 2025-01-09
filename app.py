import streamlit as st
import cv2
import numpy as np
import tempfile

# Function to count people using Haar cascade
def count_people(image):
    # Load pre-trained Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    return len(faces), faces

# Streamlit UI
st.title("Classroom People Counter")
st.write("Upload an image to count the number of people in the classroom.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_file_path = tmp_file.name

    # Load the image
    image = cv2.imread(temp_file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Count people
    count, faces = count_people(image)

    # Draw bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display results
    st.image(image, caption=f"Uploaded Image with {count} detected face(s)", use_column_width=True)
    st.success(f"Number of People Detected: {count}")
