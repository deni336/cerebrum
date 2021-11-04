from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import requests

app = Flask(__name__)
api = Api()

class Users(Resource):
    def __init__(self):
        pass
        
        

class Locations:
    def __init__(self):
        
        pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')