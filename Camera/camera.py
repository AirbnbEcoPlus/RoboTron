import cv2
from Camera import opencvmodel
from Moving import MovingController
cap = cv2.VideoCapture(10)
current_area = "Not displayed"

def generate_frames():
    while True:
        success, frame = cap.read()  # lecture de la caméra
        if not success:


            break
        else:
            results = opencvmodel.getPrevision(frame)
            # Parcourir les objets détectés et afficher leurs coordonnées
            for result in results:
                boxes = result.boxes.cpu().numpy()
                for i, box in enumerate(boxes):
                    r = box.xyxy[0].astype(int)
                    print(r)
                    milieu_x = (r[0] + r[2]) / 2
                    milieu_y = (r[1] + r[3]) / 2 
                    print("les Coordonnées du points sont " , milieu_x , " " , milieu_y)
                    if( milieu_x < 150 and milieu_x > 0):
                        MovingController.TurnRight()
                        current_area = "droite"
                    if( milieu_x > 500 and milieu_x < 640):
                        MovingController.TurnLeft()
                        current_area = "gauche"
                    if(milieu_x > 150 and milieu_x < 640):
                        if(milieu_y < 50):
                            MovingController.down()
                            current_area = "bas"
                        if(milieu_y > 50):
                            MovingController.up()
                            current_area = "haut"
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
            
            
def get_detect_area():
    return current_area


