from flask import Flask,jsonify,request
from flask_restful import Api, Resource
from pymongo import MongoClient



# create mongo client for connect mongodb and create db named visiterDb to track visitor count.

client = MongoClient("mongodb://db:27017")
db = client.newDB
visiterDb = db['visitor']
visiterDb.insert({"visit": 0})



app = Flask(__name__)
api = Api(app)



class Visit(Resource):
    def get(self):
        previousNum= visiterDb.find()[0]['visit']
        previousNum += 1
        visiterDb.update({},{"$set":{"visit":previousNum}})
        return "Hello Visitor, You are number:{}".format(previousNum)

api.add_resource(Visit,"/hello")

if __name__ == '__main__':
    app.run(debug=True, port=8008, host="0.0.0.0")

