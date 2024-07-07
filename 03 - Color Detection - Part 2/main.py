# main.py

import cv2
from PIL import Image
from util import get_limits

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Define color values in BGR format
red = [40, 20, 150]
blue = [30, 20, 150]

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the lower and upper limits for the specified color (red in this case)
    lowerLimit, upperLimit = get_limits(color=red)
    
    # Create a mask using the color limits
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    
    # Convert the mask to a PIL Image object
    mask_ = Image.fromarray(mask)
    
    # Get the bounding box of the masked area
    bbox = mask_.getbbox()

    if bbox is not None:
        # Unpack the bounding box coordinates
        x1, y1, x2, y2 = bbox

        # Draw a green rectangle around the detected object
        frameWithBbox = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        
        # Display the frame with the bounding box
        cv2.imshow("frame", frameWithBbox)
    else:
        # Display the original frame if no object is detected
        cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and close all windows (this part should be added)
cap.release()
cv2.destroyAllWindows()