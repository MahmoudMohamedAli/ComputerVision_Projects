import cv2

cap = cv2.VideoCapture(0)  # Open the default camera
out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit() 
while cap.isOpened():
    ret, frame = cap.read()  # Read the first frame to initialize   
    if ret:
        # Display the frame in a window
        cv2.imshow('Video Frame', frame)
        out.write(frame)  # Write the frame to the video file
        #cv2.waitKey(1000)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped by user.")
            break

    else:
        print("Error: Could not read frame from video device.")

cv2.destroyAllWindows()  # Close all OpenCV windows
out.release()  # Release the video writer object
cap.release()  # Release the video capture object               