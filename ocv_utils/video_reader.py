import cv2
import numpy as np


class VideoReader:
    """
    Simplifies exporting videos with opencv
    """

    def __init__(self, path="video.mp4"):

        self._video = cv2.VideoCapture(path)
        self._num_frames = int(self._video.get(cv2.CAP_PROP_FRAME_COUNT))


    def read(self, frame_id=None):

        if frame_id is not None and frame_id < self._num_frames:
            self._video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)

        ret, img = self._video.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        return ret, img



