from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.cartoony

def timestamp_now():
    datetime.utcnow()

# Interface implementation: https://stackoverflow.com/a/52960955
# class BaseModel():