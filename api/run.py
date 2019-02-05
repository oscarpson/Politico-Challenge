from flask import Flask

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello_world():
    fruits=["queens","banana","orange"]
    return "{}".format(fruits)

@app.route('/dict')
def dict():
    studs={"oscar":90,"peter":70,"queeen":12}
    marks={"oscar":190,"peter":570,"queeen":212}
    listdict=[studs,marks]
    return "{}".format(listdict)