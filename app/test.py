import requests
import json
BASE= "http://127.0.0.1:5000/"
# BASE="https://flaskapi-zs.herokuapp.com/"
# response = requests.post(BASE + "v1/product/1",{"name": "First","price":10})
# print(response)
# print(response.json())
# response = requests.put(BASE + "v1/product/1",{"name": "Updated","price":0})
# print(response)
# print(response.json())

# response = requests.delete(BASE + "v1/product/1")
# print(response)
# print(response.json())

response = requests.post(BASE + "v1/product",{"name": "First","price":10})
# response = requests.post(BASE + "v1/product/1",{"name": "First","price":10})
# response = requests.get(BASE + "v1/product/8")


print(response.json())





