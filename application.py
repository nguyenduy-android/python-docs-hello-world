from flask import Flask
from flask import request
import json
from couchbase.cluster import Cluster, PasswordAuthenticator, ClusterOptions
from couchbase.auth import PasswordAuthenticator
import base64
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return "We are teamsix"
