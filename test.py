import requests

url = 'http://localhost:5000/predict'

with open("D:/UrbanSound8K/audio/fold3/6988-5-0-2.wav", 'rb') as wav:
    files = {"file": wav}
    print(wav)
    d = {"body": "Foo Bar"}
    req = requests.post(url, files=files, json=d)

    print(req.status_code)
    print(req.text)
