import os
from PIL import Image
import pytesseract
import cv2

# Replace with your image path
image_path = "sample.jpg"
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\vedik\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe" 

# Preprocess the image (optional, but recommended)
def preprocess(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding for better contrast
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Optional: Perform additional noise reduction or deskewing

    return thresh

# Load and preprocess the image
img = cv2.imread(image_path)
preprocessed_img = preprocess(img)

# Extract text using Tesseract with configurations for handwritten text
text = pytesseract.image_to_string(preprocessed_img)

# Save extracted text to a file
with open("extracted_text.txt", "w") as f:
    f.write(text)

os.startfile("sample.jpg")
os.startfile("extracted_text.txt")
print("Handwritten text extracted and saved to 'extracted_text.txt'")