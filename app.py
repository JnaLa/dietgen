from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restx import Api, Resource, fields
app = Flask(__name__)
CORS(app)

