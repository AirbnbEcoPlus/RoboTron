from flask import Flask, render_template, Response
from Camera import camera


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/control")
def control():
    return render_template('control.html')


@app.route("/zones")
def zones():
    return render_template('zones.html')

@app.route("/detected_zone")
def detected_text():
    return Response(camera.get_detect_area())


@app.route('/camera0')
def camera0():
    return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4040', debug=True)








