from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import os
import pymongo
from bson.objectid import ObjectId
import json,bson

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



app = Flask(__name__)
# app.config["MONGO_URI"] = f"mongodb+srv://{os.environ['MONGO_USER']}:{os.environ['MONGO_PASSWORD']}@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority"

# mongo = PyMongo(app)


client = pymongo.MongoClient('mongodb+srv://admin-user-01:k99lp2MIboGTmXOq@test-cluster-01.ecwli33.mongodb.net/?retryWrites=true&w=majority')
db = client['test-cluster-01']

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    db.accounts.insert_one(data)
    return jsonify({'message': 'Data created successfully.'})

@app.route('/get/<id>', methods=['GET'])
def get(id):
    doc_id = ObjectId(id)
    data =db.accounts.find_one({'_id': doc_id})
    return JSONEncoder().encode(data)

@app.route('/getByName/<id>', methods=['GET'])
def getByName(id):
    # doc_id = ObjectId(id)
    data =db.accounts.find_one({'name': id})
    return JSONEncoder().encode(data)

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    data = request.json
    db.my_collection.update_one({'_id': id}, {'$set': data})
    return jsonify({'message': 'Data updated successfully.'})

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    db.my_collection.delete_one({'_id': id})
    return jsonify({'message': 'Data deleted successfully.'})



@app.route("/hello", methods=['GET'])
def hello():
  return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
# if __name__ == "__main__":
#   app.run()