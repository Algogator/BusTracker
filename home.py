from flask import Flask, request,json
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def hello():
    # data = request.data
    # dataDict = json.loads(data)
    # data = request.data.decode()
    # print(json.loads(data))
    data = request.get_json()
    print(data)
    return("Hello World!")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
