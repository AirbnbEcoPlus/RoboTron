import cv2
import onnxruntime as ort
import numpy as np

# Load the YOLOv8 model
net = cv2.dnn.readNetFromONNX('assets/best.onnx')

session = ort.InferenceSession('assets/best.onnx')


def getPrevisionWithRectangle(frame):
    

# Prétraiter l'image pour l'entrée du modèle
    input_name = session.get_inputs()[0].name
    image_data = cv2.resize(frame, (640, 640))
    image_data = image_data.transpose((2, 0, 1))
    image_data = image_data[np.newaxis, :, :, :].astype(np.float32)

# Effectuer une inférence sur l'image pour obtenir les boîtes de détection et les scores de confiance
    outputs = session.run(None, {input_name: image_data})
    boxes = outputs[0][0]
    scores = outputs[1][0]

# Définir un seuil de confiance pour filtrer les détections
    confidence_threshold = 0.5
    indices = np.where(scores > confidence_threshold)[0]

# Dessiner les boîtes autour des objets détectés
    for i in indices:
        box = boxes[i]
        x1, y1, x2, y2 = int(box[1] * frame.shape[1]), int(box[0] * frame.shape[0]), int(box[3] * frame.shape[1]), int(box[2] * frame.shape[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return cv2.imencode("result.png", frame)

def getPrevision(frame):
    results = model(frame)
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
