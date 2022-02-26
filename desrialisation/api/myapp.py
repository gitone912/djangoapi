import json
import requests

URL =' http://127.0.0.1:8000/s/'

data={
    'name' : 'klee',
    'roll' : 440,
    'city': 'monstad'
}

json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)