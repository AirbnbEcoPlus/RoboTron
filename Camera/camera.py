import cv2
from Camera import opencvmodel
cap = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = cap.read()  # lecture de la caméra
        if not success:

            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frame_with_detection():
    while True:
        success, frame = cap.read()  # lecture de la caméra
        if not success:

            break
        else:
            ret, buffer = opencvmodel.getPrevisionWithRectangle(frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            
def getposition_of_object():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            result = opencvmodel.getPrevision(frame)
            #Way to calc position of object
            
            
            
            correction = "right"
            return correction



