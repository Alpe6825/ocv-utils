# OCV_Utils 

Simplifies OpenCV functionalities for image and video i/o and debug-windows.

**Main Features:**
- uses _rgb_ instead of _bgr_ by default for image and video i/o
- adds a loop and boomarange mode for video capture
- imshow() accepts lists of images that will be automatically displayed next to each other, independent of their formats
- easier trackbar integration

## Install

```bash
pip3 install ocv_utils
pip3 install git+https://github.com/Alpe6825/ocv_utils
```

## Usage

### Image Loading

Load image and convert it to a certain channel type definition. Supported types `rgb`, `rgba`, `gray`

```python
from ocv_utils import load_image

img = load_image("my_image.png", channels="rgba")
```

### Video Reading

```python
from ocv_utils import VideoReader

video = VideoReader("video.mp4")

# cv2 like
while True:
    ret, frame = video.read()
    if not ret:
        break

# Or read certain frame
ret, frame = video.read(frame_id=42)
```



### Window
```python
import numpy as np
from ocv_utils import Window

window = Window(delay=0)
window.add_trackbar("x", 1, 255)
window.add_key_action(ord('h'), lambda: print("Hello World!"))

img1 = np.zeros((256, 256), dtype=np.uint8)
img2 = np.random.random((256, 256, 3))

trackbar_values = window.imshow([img1, img2])
print("Trackbar Values:", trackbar_values) # Trackbar Values: {'x': 1}

```