from pymongo import mongoClient
import os, sys, time

client = mongoClient(os.environ('MONGO_URI'))
testdb = client['test']
betadb = client['beta']
