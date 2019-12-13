import requests

#get request

response=request.get("http://localhost:5000")
print(response.text)

#posts request

requests.posts("http://localhost:5000", json={"name":"Bob"})

