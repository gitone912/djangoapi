import requests
import json

URL='http://127.0.0.1:8000'

def get_data(id=None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data=json.dumps(data)
    r = requests.get(url=URL , data= json_data)
    data=r.json()
    print(data)
get_data()

def post_data():
    data ={
        'name':'kleeenhe',
        'roll':654,
        'city':'liyue',
        
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data = json_data)
    data = r.json()
    print(data)
#post_data()

def update_data():
    data ={
        'id':2,
        'name':'kkkkkkkyaeMiko',
        'roll':84,
        'city':'liyue',
      

    }#,{'id':2,'ability':'geo'} confused here about adding multiple data
    json_data = json.dumps(data)
    r = requests.put(url=URL,data = json_data)
    data = r.json()
    
    data ={
        'id':1,
        'name':'raiden',
        'roll':84,
        'city':'inazuma',
        

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