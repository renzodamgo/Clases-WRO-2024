import cv2
from PIL import Image
from util import get_limits

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Define color values in BGR format
red = [40, 20, 150]
green = [20, 150, 20]

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create masks for both red and green
    for color in [red, green]:
        lowerLimit, upperLimit = get_limits(color=color)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            
            # Choose rectangle color based on detected color
            if color == red:
                rect_color = (0, 0, 255)  # Red in BGR
            else:
                rect_color = (0, 255, 0)  # Green in BGR
            
            # Draw a rectangle around the detected object
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), rect_color, 5)

    # Display the frame with bounding boxes
    cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()