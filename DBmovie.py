# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('mongodb+srv://yeonjae:alswo135!@cluster0.xhdde.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'name':'가버나움'},{'$set':{'star':'0'}})