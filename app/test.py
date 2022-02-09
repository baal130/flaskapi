import requests

BASE= "http://127.0.0.1:5000/"
# BASE="https://flaskapi-zs.herokuapp.com/"
response = requests.post(BASE + "v1/product/1",{"name": "First","price":10})
print(response)
print(response.json())
input()
response = requests.get(BASE + "v1/product/1")
print(response.json())