import pymongo
from dotenv import load_dotenv
from os import getenv
from flask_mongo import app

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
def hello_world():
    return 'An app for taking notes on shas!'