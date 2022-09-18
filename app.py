import numpy, requests
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        return {"ok": True}


@app.route('/test', methods=['GET'])
def send_audio():
    url = 'http://127.0.0.1:5000/predict'
    with open("D:/UrbanSound8K/audio/fold3/6988-5-0-2.wav", 'rb') as file:
        data = {'uuid': '-jx-1', 'alarmType': 1, 'timeDuration': 10}
        files = {'messageFile': file}
        req = requests.post(url, files=files, json=data)
        print(req.status_code)
        print(req.text)
    return 'some thing'


if __name__ == '__main__':
    app.run(host='192.168.1.44', port=8000)
