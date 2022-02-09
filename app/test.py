import requests

# BASE= "http://127.0.0.1:5000/"
BASE="https://flaskapi-zs.herokuapp.com/"
response = requests.post(BASE + "product/1",{"Name": "First","Price":10})
input()
response = requests.get(BASE + "product/1")
print(response.json())