from flask import Flask,request
from flask_restful import Api, Resource,reqparse
from libs.plugins import StepMethods
from pymongo import MongoClient

# create mongo client for connect mongodb and create db named User to track users.
client = MongoClient()
db = client.StorageDB
userDb = db['users']


app = Flask(__name__)
api = Api(app)

# this is for support methods e.g get data from db, authenticate user etc.
s = StepMethods()


class Register(Resource):

    def post(self):
        """
        create new username/password if its not in db else return already exists.
        :return:
        """
        reqData = request.get_json()
        username = reqData.get("Username", None)
        password = reqData.get("Password", None)

        res, result = s.is_usename_password_missing(username, password)
        if result:
            return res

        res, result = s.is_user_already_exists(username)
        if result:
            return res

        res, result = s.register_user(username,password)
        if result:
            return res


class Store(Resource):
    """
    storing simple statement for users, MAX statement can be stored 100 per user.
    """
    def post(self):
        reqData = request.get_json()
        username = reqData.get("Username", None)
        password = reqData.get("Password", None)
        statement = reqData.get("Statement", None)

        res, result = s.is_usename_password_missing(username, password)
        if result:
            return res

        # check valid username password
        res, result = s.is_authenticated(username, password)

        if result:
            res, result = s.store_statement(username, statement)
            if result:
                return res
        else:
            return res


@app.route('/statement/<user>')
def get_request(user):
    res, result = s.get_statements(user)
    return res


api.add_resource(Register, "/register")
api.add_resource(Store, "/store")


if __name__ == '__main__':
    app.run(debug=True, port=8008, host="0.0.0.0")

