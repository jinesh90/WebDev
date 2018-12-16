import json
import hashlib
from flask import Flask,jsonify,request
from pymongo import MongoClient

app = Flask(__name__)


# create mongo client for connect mongodb and create db named User to track users.
client = MongoClient("mongodb://db:27017")
db = client.StorageDB
userDb = db['users']


class StepMethods:

    def __init__(self):
        pass

    @staticmethod
    def create_response(msg, staus):
        response = app.response_class(
            response=json.dumps(msg),
            status=staus,
            mimetype='application/json'
        )
        return response

    def is_authenticated(self, username, password):

        # autheticate user
        user = userDb.find({"user": username})
        hasable = str(username) + str(password)
        calculate_hash = hashlib.md5(hasable.encode()).hexdigest()
        if len(list(user)) == 1:
            if calculate_hash == userDb.find({"user": username})[0]['password']:
                msg = {"Status" : "OK"}
                res = self.create_response(msg, 200)
                return res, True
            else:
                msg = {"Status": "Unauthorised"}
                res = self.create_response(msg, 401)
                return res, False
        else:
            msg = {"Status": "User:{} is not found".format(username)}
            res = self.create_response(msg, 404)
            return res, False

    def is_usename_password_missing(self, username,password):
        # checks for username and password.
        if username is None or password is None:
            err = {"Status": "Please Provide Username or Password."}
            res = self.create_response(err, 200)
            return res, True

        if username == "" or password == "":
            err = {"Status": "Username or Password can not be empty."}
            res = self.create_response(err, 200)
            return res, True
        return None, None

    def is_user_already_exists(self, username):
        total_users = list(userDb.find({"user": username}))
        if len(total_users) > 0:
            err = {"Status": "Username already exists.Please Select another username"}
            res = self.create_response(err, 200)
            return res, True
        return None, None

    def register_user(self, username, password):
        hasable = str(username) + str(password)
        stored_password = hashlib.md5(hasable.encode()).hexdigest()
        userDb.insert({"user": username, "password": stored_password, "statements": []})
        msg = {"Status": "Usrename :{} successfully signed up for Database Storage Service.".format(username)}
        res = self.create_response(msg, 201)
        return res, True

    def store_statement(self, username,statement):
        userDb.update({"user": username}, {"$push": {"statements": statement}})
        msg = {"Status": "Statement updated"}
        res = self.create_response(msg, 200)
        return res, True

    def get_statements(self, username):
        user = userDb.find({"user": username})
        if len(list(user)) == 1:
            user_statements = userDb.find({"user": username})[0]['statements']
            msg = {"Statements": user_statements}
            res = self.create_response(msg, 200)
            return res, True
        else:
            msg = {"Status": "User:{} is not found".format(username)}
            res = self.create_response(msg, 404)
            return res, False
