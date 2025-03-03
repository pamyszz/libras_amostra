# 🤲 Hand Gesture Recognition 🅰️🅱️
<img src="/image.png" alt="Exemplo de Detecção" width="600" />
This project uses the MediaPipe library to detect and recognize hand gestures and identify letters of the alphabet from A to E. The application uses the camera to capture hand gestures in real-time and displays the corresponding letters on the screen.

## ✨ Features
- **Gesture Recognition** 🤖: Through the camera, the system identifies hand gestures representing the letters A to E.
- **Drawing Landmarks** ✍️: MediaPipe draws the hand landmarks, allowing for a clear visualization of what is being processed.
- **Letter Display** 🔠: When a gesture is recognized, the corresponding letter is displayed on the screen.
- **Real-time Video Feed** 📹: The video feed is processed in real-time, and the letters are updated as the gestures are detected.

## 🛠️ Technologies Used
- **Python 3.x** 🐍
- **OpenCV** 📸: For video capture and image processing.
- **MediaPipe** ✋: For detecting and analyzing hand landmarks.
- **Matplotlib** 📊 (if needed for graph display, though not used in this specific code).

## ⚙️ Requirements
Make sure you have the following Python packages installed:
- `opencv-python`
- `mediapipe`
- `math` (integrated in Python)

You can install the dependencies with the following command:
```bash
pip install opencv-python mediapipe
```

## 🚀 How to Use
1. **Connect Your Camera** 📷: Ensure your camera is connected to your device. The code uses the camera located at `/dev/video1`. If necessary, adjust to the correct device.
2. **Run the Script** ▶️: Simply run the Python file. The script will open a window showing the video feed from your camera with the hand gestures being processed in real-time.
   ```bash
   python hand_gesture_recognition.py
   ```
   
3. **Recognized Gestures** 🤲:
   - **A**: Thumb up and index finger bent.
   - **B**: All fingers extended and together.
   - **C**: A "C" shape with the hand.
   - **D**: Thumb bent and the other fingers extended.
   - **E**: All fingers curled over the palm.

4. **Close the Application** ❌: To close the application, simply press the `q` key while the window is open.


## 🧑‍💻 Code Structure

- **`distance(a, b)`**: Function to calculate the Euclidean distance between two points.
- **Letter Identification Functions** 🔠: The functions `is_letter_a()`, `is_letter_b()`, `is_letter_c()`, `is_letter_d()`, and `is_letter_e()` are responsible for checking if the hand gestures correspond to one of the letters A to E.
- **Video Capture and Image Processing** 📸: The code captures images from the camera, converts them to RGB, and processes them using MediaPipe to detect hand landmarks.
- **Letter Display** 🔠: If a corresponding gesture is identified, the name of the letter is displayed on the screen.
