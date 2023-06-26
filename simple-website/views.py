from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Joey", age=21)


# creating dynamic routes
@views.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", name=username)


# querying parameters from the url
@views.route("/profilepage")
def profilepage():
    args = request.args
    name = args.get("name")
    return render_template("profile.html", name=name)


# returning json data
@views.route("/json")
def get_json():
    return jsonify({"name": "Susmita", "coolness": 10})


# getting json data from the request
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


# redirect to another page
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))
