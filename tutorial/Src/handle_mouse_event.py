import cv2
import numpy as np

def HandleMouseEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        print(f"Left button clicked at ({x}, {y})")
        cv2.putText(img, str(x) +',' +str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2)
        cv2.imshow('Image', img)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at ({x}, {y})")
        cv2.putText(img, str(x) +',' +str(y)  , (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 2)
        cv2.imshow('Image', img)

img = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black image

cv2.imshow('Image', img)  # Display the image in a window
cv2.setMouseCallback('Image', HandleMouseEvent)

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows

