from flask import Flask
from flask_pymongo import PyMongo
from flask_mongo.config import Config
# from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
# login = LoginManager(app)

from flask_mongo import routes



# @app.route('/add_meseches/<string:name>/<int:pages>/<int:item_num>')
# def add_meseches(name, pages, item_num):
#     mesechtos.insert_one({"name": name, "pages": pages, "itemNum": item_num})
#     return f"{name} added!"


