import cv2
import pytesseract

# Set the path to the tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

def extract_text(screenshot):
    # Convert the image to grayscale
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to separate text from background
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Use Tesseract to do OCR on the thresholded image
    text = pytesseract.image_to_string(thresh)
    return text

# Load the screenshot image
img = cv2.imread('screenshot.png')

# Extract text from the image
text = extract_text(img)

# Print the extracted text, if any
if text:
    print(text)
