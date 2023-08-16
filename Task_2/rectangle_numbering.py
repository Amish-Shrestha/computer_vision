import cv2
import numpy as np

# Load the image
white = np.zeros(shape=(500, 800, 3), dtype=np.uint8) + 255 # Create a white background

# Define the rectangles' coordinates (you need to provide these)
rectangles = [(50, 50, 150, 100), (200, 150, 300, 200), (350, 250, 450, 300), (100, 400, 200, 450)]

# Create a copy of the original image for drawing rectangles
image_with_rectangles = white.copy()

# Draw rectangles with numbering
for i, rectangle in enumerate(rectangles):
    x1, y1, x2, y2 = rectangle
    cv2.rectangle(image_with_rectangles, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image_with_rectangles, str(i + 1), (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

# Display the image with rectangles
cv2.imshow('Numbered Rectangles', image_with_rectangles)
cv2.waitKey(0)
cv2.destroyAllWindows()