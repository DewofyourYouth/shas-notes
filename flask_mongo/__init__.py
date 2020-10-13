from flask import Flask
from flask_mongo.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from flask_mongo import routes



# @app.route('/add_meseches/<string:name>/<int:pages>/<int:item_num>')
# def add_meseches(name, pages, item_num):
#     mesechtos.insert_one({"name": name, "pages": pages, "itemNum": item_num})
#     return f"{name} added!"


