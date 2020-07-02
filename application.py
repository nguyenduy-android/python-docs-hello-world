from flask import Flask
from flask import request
import joblib
import json
from couchbase.cluster import Cluster, PasswordAuthenticator, ClusterOptions
from couchbase.auth import PasswordAuthenticator
import base64
import pickle

cluster = Cluster('couchbase://104.215.197.138', ClusterOptions(PasswordAuthenticator('teamsix', 'FoodHotHouse@2020')))
bucket = cluster.bucket('teamsix_data')

foodmodel = None
rv = bucket.get('u:teamsixhhaimodel', quiet=True)
if rv.success:
    #print(rv.value['data'])
    savedmodel = rv.value['data'].encode('utf-8')
    savedmodel1 = base64.b64decode(savedmodel)
    #print(savedmodel1)
    foodmodel = pickle.loads(savedmodel1)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to TeamSixHHAI2020'

@app.route('/foodrecommendation',methods=['GET'])
def foodConsultant():
    if foodmodel is not None :
        foodname = request.args.get('foodname',default='Dê hấp',type=str)
        dict_result = {}
        num_result = 0
        foodname = 'Dê hấp'
        for node, _ in foodmodel.most_similar(foodname):
            dict_result.update({num_result : node})
            num_result = num_result + 1
        return json.dumps(dict_result)
    else: 
        return json.dumps({})

if __name__ == '__main__':
    app.run()
