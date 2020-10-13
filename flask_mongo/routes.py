import pymongo
from dotenv import load_dotenv
from os import getenv
from flask import render_template, flash, redirect
from flask_mongo import app
from flask_mongo.forms import LoginForm

load_dotenv()

myclient = pymongo.MongoClient(getenv("MONGODB_URI"))


sn = myclient["shasnotes"]
mesechtos = sn["meseches"]

@app.route("/show_mesechtos")
def show_mesechtos():
    ms = mesechtos.find({"$query": {}, "$orderby": {"itemNum": 1}})
    s = ""
    for doc in ms:
        s += f"{doc['name']}, {doc['pages']}\n"
    return s

@app.route('/')
def home_page():
    user = {"username": "Jacob"}
    return render_template('index.html', user=user, title="Home Page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember me={}".format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template("login.html", title="Sign In", form=form)