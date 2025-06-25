import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(layout="wide")

# Create two columns for the app
col1, col2 = st.columns([3, 2])

# Column 1: Video feed and run checkbox
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

# Column 2: Output text area
with col2:
    st.title("Answer")
    output_text_area = st.subheader("")

# Set up Generative AI model
genai.configure(api_key="API_key")
model = genai.GenerativeModel('gemini-1.5-flash')

# Set up camera capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Set up hand detector
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    """
    Get hand information from the image
    """
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0] 
        lmList = hand["lmList"]  
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers, lmList
    else:
        return None

def draw(info, prev_pos, canvas):
    """
    Draw on the canvas based on hand gestures
    """
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is not None:
            cv2.line(canvas, current_pos, prev_pos, (255, 0, 255), 10)
    elif fingers == [1, 0, 0, 0, 0]:
        canvas = np.zeros_like(img)
    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    """
    Send the canvas to the Generative AI model for math problem solving
    """
    if fingers == [0, 1, 1, 1, 1]:
        pil_image = Image.fromarray(canvas)
        try:
            response = model.generate_content(["Solve this math problem", pil_image])
            return response.text
        except google.api_core.exceptions.ResourceExhausted:
            print("Error: Resource exhausted. Please try again later.")
            return "Error: Resource exhausted. Please try again later."

# Initialize variables
prev_pos = None
canvas = None
image_combined = None
output_text = ""

while True:
    # Read camera frame
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    
    # Get hand information
    if img is not None:
        if canvas is None:
            canvas = np.zeros_like(img)
        info = getHandInfo(img)
        if info:
            fingers, lmList = info
            prev_pos, canvas = draw(info, prev_pos, canvas)
            output_text = sendToAI(model, canvas, fingers)
        
        # Combine the original image with the canvas
        image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
        FRAME_WINDOW.image(image_combined, channels="BGR")
    
    # Update output text area
    if output_text:
        output_text_area.text(output_text)
    
    # Wait for a short period
    cv2.waitKey(1)