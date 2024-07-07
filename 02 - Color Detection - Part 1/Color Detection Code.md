# Tutorial: Red Object Detection with OpenCV

## Step 1: Set up the environment

- Install the required libraries: OpenCV (opencv-python), Pillow (PIL), and NumPy.
- Create a new Python file for your project.

## Step 2: Import necessary modules

```python
import cv2

from PIL import Image

  

from util import get_limits

  
  

red = [40, 20, 150] # red in BGR colorspace

cap = cv2.VideoCapture(0)

while True:

ret, frame = cap.read()

  

hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  

lowerLimit, upperLimit = get_limits(color=red)

  

mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

  

mask_ = Image.fromarray(mask)

  

bbox = mask_.getbbox()

  

if bbox is not None:

x1, y1, x2, y2 = bbox

  

frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

  

cv2.imshow('frame', frame)

  

if cv2.waitKey(1) & 0xFF == ord('q'):

break

  

cap.release()

  

cv2.destroyAllWindows()
```


```python

```


```python

```


```python

```


```python

```

```python

```

```python

```