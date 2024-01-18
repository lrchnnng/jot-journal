import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    entries = mongo.db.entries.find()
    return render_template("index.html", entries=entries)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        if existing_user and check_password_hash(existing_user["password"], request.form.get("password")):
            session["user_id"] = str(existing_user["_id"])
            session["user"] = existing_user["username"]
            flash("Welcome to Jot, {}".format(existing_user["username"]))
            return redirect(url_for("profile", username=existing_user["username"]))

        else:
            # username doesn't exist or password is incorrect
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")
    

@app.route("/logout")
def logout():
    #remove user from session cookie
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Ensure the user is logged in
    if "user_id" not in session:
        return redirect(url_for("login"))

    # grab the session user's user_id from the session
    user_id = ObjectId(session["user_id"])

    # find entries for the current user using user_id
    entries = mongo.db.entries.find({"user_id": user_id})

    if session["user"]:
        return render_template("profile.html", username=username, entries=entries)

    return redirect(url_for("login"))


 
@app.route("/create_entry", methods=["GET", "POST"])
def create_entry():
    if request.method == "POST":
        entry = {
            "date": request.form.get("date"),
            "title": request.form.get("title"),
            "main_entry": request.form.get("main_entry"),
            "answer_1a": request.form.get("answer_1a"),
            "answer_1b": request.form.get("answer_1b"),
            "answer_1c": request.form.get("answer_1c"),
            "answer_2a": request.form.get("answer_2a"),
            "answer_2b": request.form.get("answer_2b"),
            "answer_2c": request.form.get("answer_2c"),
            "day_rating": request.form.get("day_rating"),
            }
        mongo.db.entries.insert_one(entry)
        flash("Entry Successfully Added")
        return redirect(url_for('profile', username=session['user']))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_entry.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)