import cv2
import numpy as np
from elements.yolo import OBJ_DETECTION


Object_classes = ["people", "pedestrian", "human"]

Object_detector = OBJ_DETECTION("weights/son.pt", Object_classes)


def detect(frame):
    # detection process
    objs = Object_detector.detect(frame)
    xy = []
    detections = []

    # plotting
    for obj in objs:

        [(xmin, ymin), (xmax, ymax)] = obj["bbox"]
        detections.append([xmin, ymin, xmax, ymax])
        x = (xmax - xmin) / 2 + xmin
        y = (ymax - ymin) / 2 + ymin

        xy.append([int(x), int(y)])

    if len(xy) > 0:
        a = detections[0]
        cv2.rectangle(frame, (a[0], a[1]), (a[2], a[3]), (0, 255, 0), 2)

    return xy
