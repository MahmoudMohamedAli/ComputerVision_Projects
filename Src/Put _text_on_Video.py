import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)  # Open the default camera

text = 'Hello, OpenCV'    # Text to be displayed
fpstext = 'fps' +   str(cap.get(cv2.CAP_PROP_FPS)) # Additional instructions 

exittext = 'Press "q" to stop recording'  # Additional instructions 

while cap.isOpened():
    ret, frame = cap.read()  # Read the first frame to initialize   
    if ret:
        # Add text to the frame
        datetext = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, fpstext, (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, datetext, (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, exittext, (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Display the frame in a window
        cv2.imshow('Video Frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped by user.")
            break

    else:
        print("Error: Could not read frame from video device.")
