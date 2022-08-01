import requests

r = requests.post("http://localhost:5000/predict", json={"z": 5, "y": 10})

try:
    print(r.json())
except Exception:
    print(r.content)