# CRUD API with Flask, PostgreSQL, Docker and Docker Compose
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)  # create instance of Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")  # set the database URI

db = SQLAlchemy(app)  # create instance of SQLAlchemy


class User(db.Model):
    __tablename__ = "users"  # set the table name

    id = db.Column(db.Integer, primary_key=True)  # set the column id
    username = db.Column(db.String(80), nullable=False)  # set the column name
    email = db.Column(db.String(120), nullable=False)  # set the column email

    def json(self):
        return {"id": self.id, "username": self.username, "email": self.email}


db.create_all()  # create the table


# create a test route
@app.route("/test", methods=["GET"])
def test():
    return make_response(jsonify({"message": "Test route"}), 200)


# create a user route
@app.route("/user", methods=["POST"])
def create_user():
    try:
        data = request.get_json()  # get the data from the request
        # create a user object
        new_user = User(username=data["username"], email=data["email"])
        db.session.add(new_user)  # add the user to the session
        db.session.commit()  # commit the session
        # return a response
        return make_response(jsonify({"message": "User created"}), 201)
    except Exception as e:
        return make_response(jsonify({"message": "Error creating user"}), 500)


# get all users route
@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()  # get all users
        # return a response
        return make_response(jsonify({"users": [user.json() for user in users]}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error getting users"}), 500)


# get a user route by id
@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    try:
        # get a user by id
        user = User.query.filter_by(id=id).first()
        if user:
            # return a response
            return make_response(jsonify({"user": user.json()}), 200)
        else:
            # return a response
            return make_response(jsonify({"message": "User not found"}), 404)
    except Exception as e:
        return make_response(jsonify({"message": "Error getting user"}), 500)


# update a user
@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()  # get a user by id
        if user:
            data = request.get_json()
            user.username = data["username"]  # update the username
            user.email = data["email"]  # update the email
            db.session.commit()  # commit the session
            # return a response
            return make_response(jsonify({"message": "User updated"}), 200)
        else:
            # return a response
            return make_response(jsonify({"message": "User not found"}), 404)
    except Exception as e:
        return make_response(jsonify({"message": "Error updating user"}), 500)


# delete a user
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()  # get a user by id
        if user:
            db.session.delete(user)  # delete the user
            db.session.commit()  # commit the session
            # return a response
            return make_response(jsonify({"message": "User deleted"}), 200)
        else:
            # return a response
            return make_response(jsonify({"message": "User not found"}), 404)
    except Exception as e:
        return make_response(jsonify({"message": "Error deleting user"}), 500)
