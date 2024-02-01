# Hand Gesture Calculator
This is a simple calculator program that allows users to perform basic arithmetic operations using hand gestures captured through a webcam. The application detects hand movements and calculates expressions based on the user's interactions with on-screen buttons.

# Features
- **Hand Gesture Recognition:** Utilizes the OpenCV library and the cvzone HandTrackingModule to detect and track hand movements.
- **On-screen Calculator Buttons:** Displays a set of calculator buttons on the screen, each representing a digit or an arithmetic operation.
- **Dynamic Font Sizing:** Adjusts the font size of the equation display dynamically based on the length of the expression.
- **AC (All Clear) Functionality:** Allows users to delete the last entered character or clear the entire expression.
- **Real-time Calculation:** Computes the result of the mathematical expression in real-time.

# Getting Started
**Prerequisites**
- Python 3.7 version
- OpenCV (cv2) library
- cvzone library (HandTrackingModule)
# Installation
**Clone the repository:**
git clone https://github.com/TahaAhmet/Virtual-Calculator.git

**Install the required libraries:**
- pip install opencv-python
- pip install cvzone

# Usage
**Run the calculator.py script:**
- python calculator.py
- Ensure that your webcam is enabled and properly configured.
- Interact with the calculator using your hand gestures to input and calculate expressions.

# Controls
- Use your hand to hover over the on-screen calculator buttons.
- Pinch your thumb and index finger to simulate a button click.
- Perform a pinch gesture near the "AC" button to delete the last character or clear the entire expression.
# Notes
- Press 'q' on the keyboard to exit the application.
