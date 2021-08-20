# To run postman go to collections on right side

from flask import Flask,jsonify, request # jsonify because we are using js noatation

app = Flask(__name__)

tasks = [
    {
        'id': 1,  # suggesting that this is first task
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

# adding the data using post method i.e sending some data to server
# to the URL just append /get-data you will get this output
@app.route("/add-data", methods=["POST"])     
def add_task():
     # if the request is not json it will show 404 error that Please provide the data
    if not request.json:  
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
         #this will make your task start from task[0] 
        'id': tasks[-1]['id'] + 1, 
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)