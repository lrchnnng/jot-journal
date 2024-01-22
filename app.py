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
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
 
 
@app.route("/create_entry", methods=["GET", "POST"])
def create_entry():
    if request.method == "POST":
        recommend = "on" if request.form.get("recommended") else "off"
        entry = {
            "entry_title": request.form.get("entry_title"),
            "review_date": request.form.get("review_date"),
            "book_title": request.form.get("book_title"),
            "author_name": request.form.get("author_name"),
            "genres": request.form.get("genre_name"),
            "review": request.form.get("review"),
            "publish_date": request.form.get("publish_date"),
            "publisher": request.form.get("publisher"),
            "recommended": recommend,
            "review_by": session["user"],
            }
        mongo.db.entries.insert_one(entry)
        flash("Entry Successfully Added")
        return redirect(url_for('index', username=session['user']))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("create_entry.html", genres=genres)


@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_entry.html", entry=entry, genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)