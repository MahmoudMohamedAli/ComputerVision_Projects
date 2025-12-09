import cv2
import numpy as np  

def HandleMouseEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
        cv2.circle(image, (x, y), 5, (255, 255, 255), -1)
        points.append((x, y))
        if len(points) > 1:
            cv2.line(image, points[-2], points[-1], (255, 255, 255), 2)
        cv2.imshow('Image', image)

        #cv2.putText(image, str(x) + ',' + str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        #cv2.imshow('Image', image)


points = []
image = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black image 
cv2.imshow('Image', image)  # Display the image in a window
cv2.setMouseCallback('Image', HandleMouseEvent) 
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
