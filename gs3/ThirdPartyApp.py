import requests
import json
URL="http://127.0.0.1:8000/stucreate/"
data={'name' : 'Subham', 'roll':105, 'city':'Banglore'}
json_data=json.dumps(data) #To convert python to json data
x=requests.post(url=URL, data=json_data)
data=x.json()
print(data)