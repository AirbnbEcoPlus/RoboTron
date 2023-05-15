import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model
#net = cv2.dnn.readNetFromONNX('assets/best.onnx')

#session = ort.InferenceSession('assets/best.onnx')
model = YOLO('./assets/best.pt')

def getPrevisionWithRectangle(frame):
    results = model(frame)
    return results[0].plot()


def getPrevision(frame):
    results = model(frame, imgsz=128)
    return results

def IfObjectDetected(results):
    for results in results:
        if(results['label']) == "trousse":
            object_found = True
            break

    if(object_found):
        return True
    else:
        return False


def MovementController(frame):
    results = getPrevision(frame)
    
