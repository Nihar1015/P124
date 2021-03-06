
from flask import Flask,jsonify,request
app = Flask(__name__)

    

data = [
    {
        'id':1,
        'Contact': '9987644456',
        'Name': u'Raju',
        'done': False
    },
    {
        'id': 2,
        'Contact': u'9876543222',
        'Name': u'Rahul',
        'done': False
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
    
        },400)
    
    task ={
        'id':data[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done':False

    }

    data.append(task)
    return jsonify({
        "status": "Success",
        "message": "Task added succesfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": data
    })

if (__name__ == "__main__"):
    app.run(debug = True)
