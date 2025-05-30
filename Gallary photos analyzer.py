import os
import cv2
import numpy as np
from PIL import Image
import pytesseract
import imagehash
import matplotlib.pyplot as plt  # Import for displaying images
from sklearn.cluster import DBSCAN

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# --- Configuration ---
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# --- Image Loader ---
def load_images(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(IMAGE_EXTENSIONS)]

# --- OCR Text Extraction ---
def extract_text(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

# --- Duplicate Detection ---
def find_duplicates(image_paths):
    hashes = {}
    duplicates = []
    for path in image_paths:
        img = Image.open(path)
        hash_val = imagehash.average_hash(img)
        if hash_val in hashes:
            duplicates.append((path, hashes[hash_val]))
        else:
            hashes[hash_val] = path
    return duplicates

# --- Blur Detection ---
def is_blurry(image_path, threshold=100):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return False
    laplacian = cv2.Laplacian(img, cv2.CV_64F).var()
    return laplacian < threshold

# --- Face Detection with OpenCV (No dlib required) ---
def detect_faces_opencv(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        print(f"Faces detected in {image_path}")
        return True
    else:
        return False

# --- Function to Display Image ---
def display_image(image_path, title="Image"):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert color for correct display in matplotlib
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')  # Hide axes
    plt.show()

# --- Main Runner ---
def analyze_gallery(folder):
    print(f"Analyzing folder: {folder}\n")
    image_paths = load_images(folder)

    print("\n1. Detecting duplicate images...")
    duplicates = find_duplicates(image_paths)
    for dup in duplicates:
        print(f"Duplicate found: {dup[0]} and {dup[1]}")
        # Display the duplicate images
        display_image(dup[0], title="Duplicate Image 1")
        display_image(dup[1], title="Duplicate Image 2")

    print("\n2. Detecting blurry images...")
    for path in image_paths:
        if is_blurry(path):
            print(f"Blurry image: {path}")
            # Display the blurry image
            display_image(path, title="Blurry Image")

    print("\n3. Extracting text from images...")
    for path in image_paths:
        text = extract_text(path).strip()
        if text:
            print(f"Text in {path}:")
            print(text)
            # Display the image with extracted text
            display_image(path, title="Image with Extracted Text")

    print("\n4. Detecting faces using OpenCV...")
    for path in image_paths:
        detect_faces_opencv(path)
        # Display the image with detected faces (if any)
        display_image(path, title="Face Detected Image")

# --- Run the analyzer ---
if __name__ == "__main__":
    analyze_gallery(r"c:\Users\milly\OneDrive\Desktop\images")  # Correct path to your image folder
