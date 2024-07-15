import requests

response=requests.post("http://0.0.0.0:8000/record", json={"engine_temperature": 0.3})

print(response.json())
