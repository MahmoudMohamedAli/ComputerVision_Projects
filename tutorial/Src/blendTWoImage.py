import cv2
import numpy as np

img1 = cv2.imread('Resources/lena.jpg')  # Load an image from file
img2  = cv2.imread('Resources/aero1.jpg')  # Load an image from file

print("Image 1 shape:", img1.shape)  # Print the shape of the first image
print("Image 2 shape:", img2.shape)  # Print the shape of the second

img2  = cv2.resize(img2, (img1.shape[1], img1.shape[0]), interpolation=cv2.INTER_AREA)  # Resize the second image to match the first image's dimensions

res = cv2.addWeighted(img1, 0.3, img2, 0.7,0)  # Blend the two images using addWeighted
cv2.imshow('Blended Image', res)  # Display the blended image in a window
cv2.waitKey(0)  # Wait for a key press to close the window  
cv2.destroyAllWindows()  # Close all OpenCV windows