import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')  # Load an image from file
img = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 5)  # Draw a blue line from top-left to bottom-right
img = cv2.arrowedLine(img, (0, img.shape[0]), (img.shape[1], 0), (0, 255, 0), 5)  # Draw a green arrowed line from bottom-left to top-right
img = cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 100, (0, 0, 255), 5)  # Draw a red circle at the center of the image

img =cv2.rectangle(img, (100, 100), (300, 300), (255, 255, 0), 5)  # Draw a cyan rectangle covering the entire image
img = cv2.putText(img, 'OpenCV Drawing', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)  # Add white text to the image

cv2.imshow('Drawn Image', img)  # Display the modified image in a window
cv2.waitKey(0)  # Wait for a key press to close the window  
cv2.destroyAllWindows()  # Close all OpenCV windows
