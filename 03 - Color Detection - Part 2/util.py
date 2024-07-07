# util.py

import numpy as np
import cv2

def get_limits(color):
    """
    Calculate the lower and upper HSV limits for a given BGR color.
    
    Args:
    color (list): A list of three integers representing a color in BGR format.
    
    Returns:
    tuple: Two numpy arrays representing the lower and upper HSV limits.
    """
    # Convert the BGR color to a numpy array of shape (1,1,3)
    c = np.uint8([[color]])
    
    # Convert the BGR color to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Extract the Hue value
    hue = hsvC[0][0][0]
    
    # Calculate the lower limit by subtracting 10 from the Hue
    lowerLimit = np.array([hue - 10, 100, 100])
    
    # Calculate the upper limit by adding 10 to the Hue
    upperLimit = np.array([hue + 10, 255, 255])
    
    return lowerLimit, upperLimit