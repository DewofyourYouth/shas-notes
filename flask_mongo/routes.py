import pymongo
from dotenv import load_dotenv
from os import getenv
from flask import render_template, flash, redirect, session, request, url_for
from flask_mongo import app, mongo
from flask_mongo.forms import LoginForm, RegisterForm
import bcrypt
import pprint

load_dotenv()

myclient = pymongo.MongoClient(getenv("MONGODB_URI"))


sn = myclient["shasnotes"]
mesechtos = sn["meseches"]


@app.route("/show_mesechtos")
def show_mesechtos():
    ms = mesechtos.find({"$query": {}, "$orderby": {"itemNum": 1}})
    s = ""
    for doc in ms:
        s += f"{doc['hebName']}, {doc['pages']}\n"
    return s


@app.route("/")
def index():
    try:
        name = session["first_name"]
        username = session["username"]
    except KeyError:
        name = "user"

    if name != "user":
        user = mongo.db.users.find_one({"username": username})

        learning = []
        if user.get("learning") is not None:
            for m in user.get("learning"):
                ms = mongo.db.meseches.find_one({"name": m})
                if ms:
                    learning.append(ms)

    return render_template("index.html", name=name, learning=learning, title="Home Page")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        users = mongo.db.users
        form_username, first_name, last_name, password = request.form["username"], request.form["first_name"], request.form["last_name"], request.form["password"].encode("utf-8")
        existing_user = users.find_one({"username": form_username})

        if existing_user is None:
            hashpass = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
            users.insert({"username": form_username, "firstName": first_name, "lastName": last_name, "pwd": hashpass})
            session["username"] = form_username
            session["first_name"] = first_name
            return redirect(url_for("index"))
        return "That username already exists!"
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    # if request.method == 'POST':
    #     users = mongo.db.users
    #     login_user = users.find_one({"username": request.form["username"]})
    #     if login_user:
    #         if bcrypt.checkpw(request.form['password'])

    form = LoginForm()
    if form.validate_on_submit():
        users = mongo.db.users
        login_user = users.find_one({"username": form.username.data})
        if login_user:
            if bcrypt.checkpw(form.password.data.encode("utf-8"), login_user["pwd"]):
                pass
            else:
                flash("Wrong password")
                return redirect("/login")
        else:
            flash("That user does not exist, register a new user?")
            return redirect("/register")
        session["username"] = login_user["username"]
        session["first_name"] = login_user["firstName"]
        session["is_authenicated"] = True
        print(login_user)
        flash("Login requested for user {}, remember me={}".format(form.username.data, form.remember_me.data))
        return redirect("/")
    return render_template("login.html", title="Sign In", form=form)

@app.route('/add_note')
def add_note():
    return render_template('addnote.html')