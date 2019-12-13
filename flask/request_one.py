from flask import Flask
import requests

#get request

response=requests.get("http://localhost:5000")
print(response.text)

#posts request

requests.post("http://localhost:5000", json={"name":"Bob"})

