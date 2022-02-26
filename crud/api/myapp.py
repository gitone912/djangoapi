import requests
import json

URL='http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data=json.dumps(data)
    r = requests.get(url=URL , data= json_data)
    data=r.json()
    print(data)
#get_data()

def post_data():
    data ={
        'name':'qiqi',
        'roll':454,
        'city':'liyue',
        'ability':'cryo'

    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data = json_data)
    data = r.json()
    print(data)
post_data()

def update_data():
    data ={
        'id':1,
        'name':'yaeMiko',
        'roll':84,
        'city':'liyue',
        'ability':'electro'

    }#,{'id':2,'ability':'geo'} confused here about adding multiple data
    json_data = json.dumps(data)
    r = requests.put(url=URL,data = json_data)
    data = r.json()
    
    data ={
        'id':3,
        'name':'raiden',
        'roll':84,
        'city':'inazuma',
        'ability':'electro'

    }#,{'id':2,'ability':'geo'} confused here about adding multiple data
    json_data = json.dumps(data)
    r = requests.put(url=URL,data = json_data)
    data = r.json()
    
    print(data)
#update_data()
def delete_data():
    data ={
        'id':1}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data = json_data)
    data = r.json()
    print(data)
#delete_data()