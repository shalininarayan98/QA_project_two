from flask import Flask, request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def get_test():
    return {"name": "Bob"}

@app.route('/post_test', methods=['GET','POST'])
def post_test():
    print(request.json)
    return "ok"

if (__name__ == '__main__'):
    app.run(port=5000, host='0.0.0.0')
