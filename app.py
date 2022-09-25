from flask import Flask, request, flash
import tensorflow as tf
import numpy as np
import os
import librosa
from werkzeug.utils import secure_filename

# from flask_pymongo import PyMongo

model = tf.keras.models.load_model('model.h5')

ALLOWED_EXTENSIONS = {'wav', 'mp3', 'mp4', 'm4a'}
UPLOAD_FOLDER = 'D:/yaman/project/emergency/UPLOAD_FOLDER'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return 'Hello World!'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['audio_file']
        if file.filename == '':
            flash('No selected file')
            return 'No file selected'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        def feature_extractor(path):
            audio, sample_rate = librosa.load(path, res_type="kaiser_fast")
            mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
            return mfccs_scaled_features

        path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        returngot = feature_extractor(path)
        returngot = returngot.reshape(1, -1)
        predictions = (model.predict(returngot) > 0.5).astype("int32")

        print(path)
        os.remove(path)
        if predictions[0][0] == 0:
            return {"Prediction": 'Emergency'}
        else:
            return {"Prediction": 'Non Emergency'}

    return {'file': 'empty'}


if __name__ == '__main__':
    app.run()
