# OCV-Utils 

## Install



## Utils

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