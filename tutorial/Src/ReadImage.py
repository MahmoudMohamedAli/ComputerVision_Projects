import cv2

# Print the OpenCV version

print("OpenCV version:", cv2.__version__)   

# Load an image
image = cv2.imread('lena.jpg',-1)
# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")       
else:
    # Display the image in a window
    cv2.imshow('Lena Image', image)
    cv2.imwrite('output_image.jpg', image)  # Save the image to a file
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()