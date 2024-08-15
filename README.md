## Playing FireBoy and WaterGirl using Hand Sign Recognition

<p align="center">
  <img src="images-1.jpeg" alt="alt text" />
</p>


This is a simple project for personal study on using popular computer vision libraries and open-source ML models.

- OpenCV is used for webcam connection and drawing hand landmarks.
- MediaPipe is used for machine learning.
- PyAutoGUI is used for inputting keyboard commands.

## How to Play

- Clone this repository.
- Install the required packages using `pip install -r requirements.txt`.
- Run `main.py`.
- Open the game on any website using your browser.
- Make sure to select your browser window with the OpenCV video running.
- Give hand signs to move the characters.

## Commands

Your right hand is supposed to send commands to WaterGirl, controlling "wsd" keys with the following mapping:
- Pointing Up for `d` (Running to the right)
- Victory sign for `a` (Running to the left)
- Closed Fist for `w` (Jumping)
- Open Palm to cancel all movement (Stop)
  
Your left hand is supposed to send commands to FireBoy, controlling "→←↑" keys with:
- Pointing Up for `→` (Running to the right)
- Victory sign for `←` (Running to the left)
- Closed Fist for `↑` (Jumping)
- Open Palm to cancel all movement (Stop)

If you want to change which hand controls which character, you need to hard-code the keys passed to PyAutoGUI's `KeyDown` and `KeyUp` methods.

## Useful Information

The parameter `pyautogui.PAUSE = 0` is needed to eliminate the delay that PyAutoGUI automatically implements to prevent mouse lock when automating mouse clicks.

You can find information about the ML model directly in this link: https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer

## Documentation

- MediaPipe: https://ai.google.dev/edge/mediapipe/solutions/guide
- OpenCV: https://opencv.org
- PyAutoGui: https://pyautogui.readthedocs.io/en/latest/
