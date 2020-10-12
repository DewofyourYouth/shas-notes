import pymongo
from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
myclient = pymongo.MongoClient(getenv("MONGODB_URI"))


sn = myclient["shasnotes"]
mesechtos = sn["meseches"]

@app.route('/add_meseches/<string:name>/<int:pages>/<int:item_num>')
def add_meseches(name, pages, item_num):
    mesechtos.insert_one({"name": name, "pages": pages, "itemNum": item_num})
    return f"{name} added!"

@app.route("/show_mesechtos")
def show_mesechtos():
    ms = mesechtos.find({"$query": {}, "$orderby": {"itemNum": 1}})
    s = ""
    for doc in ms:
        s += f"{doc['name']}, {doc['pages']}\n"
    return s

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)