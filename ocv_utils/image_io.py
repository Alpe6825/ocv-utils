import cv2
import numpy as np


def load_image(path, channels="rgb", size=None):

    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    if channels == "rgb":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif channels == "rgba":
        alpha = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 1, 255, cv2.THRESH_BINARY)[1]
        alpha = alpha.reshape(alpha.shape[0], alpha.shape[1], 1)
        image = np.concatenate((image, alpha), axis=2)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    elif channels == "gray":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        raise ValueError("Undefined channel combination")

    if size is not None:
        image = cv2.resize(image, size)

    return image
