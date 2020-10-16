from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = getenv("SECRET_KEY")
    MONGO_DBNAME = getenv("MONGO_DBNAME")
    MONGO_URI= getenv("MONGO_URI")