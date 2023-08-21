import cv2

# Load the image
image_path = '/media/user/New Volume/Computer Vision/Task_2/image.png'
image = cv2.imread(image_path)
# Resize the image if needed
image = cv2.resize(image, (800, 1200))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
# Apply Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter rectangles based on shape properties (e.g., four sides)
rectangles = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    if len(approx) == 4:
        rectangles.append(approx)

# Define your length thresholds for assigning numbers
threshold1 = 400  # Adjust this threshold based on your criteria
threshold2 = 400  # Adjust this threshold based on your criteria

# Measure the length of each rectangle and number them
for i, rect in enumerate(rectangles):
    x, y, w, h = cv2.boundingRect(rect)
    length = max(w, h)  # Measure length based on the longer side

    # Assign numbers based on length thresholds
    if length < threshold1:
        number = 1
    elif length < threshold2:
        number = 2
    else:
        number = 3

    # Draw the assigned number on the rectangle
    cv2.putText(image, str(number), (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the image with numbered rectangles
cv2.imshow('Numbered Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
