import cv2 as cv
import mediapipe as mp
import pyautogui
import time

pyautogui.PAUSE = 0

translation_dict = {
                    'Pointing_Up':'Indicador (Andar)',
                    'Victory':'Indicador e Medio (Recuar)',
                    'Closed_Fist':'Punho (Pular)'
                    }

key_dict_right = {'Open_Palm':None,
                    'Pointing_Up':'d',
                    'Victory':'a',
                    'Closed_Fist':'w'
                    }

key_dict_left = {'Open_Palm':None,
                    'Pointing_Up':'right',
                    'Victory':'left',
                    'Closed_Fist':'up'
                    }

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands()

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_file = open('gesture_recognizer.task', "rb")
model_data = model_file.read()
model_file.close()

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_buffer=model_data),
    running_mode=VisionRunningMode.VIDEO,
    num_hands = 2
)
with GestureRecognizer.create_from_options(options) as recognizer:
    cap = cv.VideoCapture(0)
    
    timestamp = 0
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

            results_recognizer = recognizer.recognize_for_video(mp_image, timestamp)
            if results_recognizer.gestures:
                first_hand_gesture = None
                first_hand_label = None
                second_hand_gesture = None
                second_hand_label = None
                if len(results.multi_handedness) == 1 and len(results_recognizer.gestures) == 1:
                    first_hand_label = results.multi_handedness[0].classification[0].label
                    first_hand_gesture = results_recognizer.gestures[0][0].category_name

                    if first_hand_label == 'Right':
                        cv.putText(frame, f'Direita: {translation_dict.get(first_hand_gesture)}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
                        if first_hand_gesture == 'Pointing_Up':
                            pyautogui.keyUp('a')
                            pyautogui.keyDown('d')

                        elif first_hand_gesture == 'Victory':
                            pyautogui.keyUp('d')
                            pyautogui.keyDown('a')

                        elif first_hand_gesture == 'Closed_Fist':
                            pyautogui.keyDown('w')
                            time.sleep(0.05)
                            pyautogui.keyUp('w')

                    elif first_hand_label == 'Left':
                        cv.putText(frame, f'Esquerda: {translation_dict.get(first_hand_gesture)}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                        if first_hand_gesture == 'Pointing_Up':
                            pyautogui.keyUp('left')
                            pyautogui.keyDown('right')

                        elif first_hand_gesture == 'Victory':
                            pyautogui.keyUp('right')
                            pyautogui.keyDown('left')

                        elif first_hand_gesture == 'Closed_Fist':
                            pyautogui.keyDown('up')
                            time.sleep(0.05)
                            pyautogui.keyUp('up')

                if len(results.multi_handedness) == 2 and len(results_recognizer.gestures) == 2:
                    first_hand_label = results.multi_handedness[1].classification[0].label
                    first_hand_gesture = results_recognizer.gestures[0][0].category_name

                    second_hand_label = results.multi_handedness[0].classification[0].label
                    second_hand_gesture = results_recognizer.gestures[1][0].category_name

                    if first_hand_label == 'Right':
                        cv.putText(frame, f'Direita: {translation_dict.get(first_hand_gesture)}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
                        cv.putText(frame, f'Esquerda: {translation_dict.get(second_hand_gesture)}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

                        if first_hand_gesture == 'Pointing_Up':
                            pyautogui.keyUp('a')
                            pyautogui.keyDown('d')

                        elif first_hand_gesture == 'Victory':
                            pyautogui.keyUp('d')
                            pyautogui.keyDown('a')

                        elif first_hand_gesture == 'Closed_Fist':
                            pyautogui.keyDown('w')
                            time.sleep(0.05)
                            pyautogui.keyUp('w')

                        if second_hand_gesture == 'Pointing_Up':
                            pyautogui.keyUp('left')
                            pyautogui.keyDown('right')

                        elif second_hand_gesture == 'Victory':
                            pyautogui.keyUp('right')
                            pyautogui.keyDown('left')

                        elif second_hand_gesture == 'Closed_Fist':
                            pyautogui.keyDown('up')
                            time.sleep(0.05)
                            pyautogui.keyUp('up')

                    elif first_hand_label == 'Left':
                        cv.putText(frame, f'Direita: {translation_dict.get(second_hand_gesture)}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
                        cv.putText(frame, f'Esquerda: {translation_dict.get(first_hand_gesture)}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

                        if first_hand_gesture == 'Pointing_Up':
                            pyautogui.keyUp('left')
                            pyautogui.keyDown('right')

                        elif first_hand_gesture == 'Victory':
                            pyautogui.keyUp('right')
                            pyautogui.keyDown('left')

                        elif first_hand_gesture == 'Closed_Fist':
                            pyautogui.keyDown('up')
                            time.sleep(0.05)
                            pyautogui.keyUp('up')

                        if second_hand_gesture == 'Pointing_Up':
                            pyautogui.keyUp('a')
                            pyautogui.keyDown('d')

                        elif second_hand_gesture == 'Victory':
                            pyautogui.keyUp('d')
                            pyautogui.keyDown('a')

                        elif second_hand_gesture == 'Closed_Fist':
                            pyautogui.keyDown('w')
                            time.sleep(0.05)
                            pyautogui.keyUp('w')

                if first_hand_gesture == 'Open_Palm':
                    if first_hand_label == 'Right':
                        pyautogui.keyUp('w')
                        pyautogui.keyUp('d')
                        pyautogui.keyUp('a')
                        
                    elif first_hand_label == 'Left':
                        pyautogui.keyUp('up')
                        pyautogui.keyUp('right')
                        pyautogui.keyUp('left')

                if second_hand_gesture == 'Open_Palm':
                    if second_hand_label == 'Right':
                        pyautogui.keyUp('w')
                        pyautogui.keyUp('d')
                        pyautogui.keyUp('a')
                    elif second_hand_label == 'Left':
                        pyautogui.keyUp('up')
                        pyautogui.keyUp('right')
                        pyautogui.keyUp('left')
                        

        desired_width = 750
        desired_height = 500
        resized_frame = cv.resize(frame, (desired_width, desired_height))
        cv.imshow('Gesture Recognition', resized_frame)
        
        if cv.waitKey(1) == ord('q'):
            break

        timestamp += 1

    cap.release()
    cv.destroyAllWindows()
