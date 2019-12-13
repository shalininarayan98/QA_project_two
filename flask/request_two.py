from flask import Flask
import requests

app=Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    requests.post('http://localhost:5000', json={"name":"Bob"})
    return "ok\n"

if __name__=='__main__':
    app.run(port=5001, host='0.0.0.0')

