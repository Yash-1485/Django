# import pymongo as pm
# import environ, os
# env = environ.Env()
# environ.Env.read_env(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# client=pm.MongoClient(env('MONGODB_CONNECTION'))

# db=client['testDjango_Mongo']
from mongoengine import connect
# connect('project1')
connect(host="mongodb+srv://yashparekh140805:v0qJv69Hcgc6ihpr@cluster0.if4setw.mongodb.net/stackchat_db?retryWrites=true&w=majority&appName=Cluster0")