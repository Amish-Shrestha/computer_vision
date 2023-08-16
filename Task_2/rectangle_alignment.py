import cv2
import numpy as np

# Load the image
white = np.zeros(shape=(500, 800, 3), dtype=np.uint8) + 255  # Create a white background

# Define the rectangles' coordinates (you need to provide these)
rectangles = [(50, 200, 150, 250), (200, 200, 300, 250), (350, 200, 450, 250), (500, 200, 600, 250)]

# Create a copy of the original image for drawing rectangles
image_with_rectangles = white.copy()

# Draw rectangles with numbering
for i, rectangle in enumerate(rectangles):
    x1, y1, x2, y2 = rectangle
    cv2.rectangle(image_with_rectangles, (x1, y1), (x2, y2), (0, 255, 0), 2)
    rect_center = ((x1 + x2) // 2, (y1 + y2) // 2)
    cv2.putText(image_with_rectangles, str(i + 1), rect_center, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

# Display the image with rectangles
cv2.imshow('Numbered Rectangles', image_with_rectangles)
cv2.waitKey(0)
cv2.destroyAllWindows()