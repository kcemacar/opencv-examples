from flask import Flask, render_template, Response
import cv2
from cascade import mycascade

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

app = Flask(__name__)
camera = cv2.VideoCapture(0) 

@app.route('/video_feed')
def video_feed():
    return Response(mycascade(camera, face_cascade), mimetype='multipart/x-mixed-replace; boundary=frame')
#Video streaming route. Put this in the src attribute of an img tag

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) 
