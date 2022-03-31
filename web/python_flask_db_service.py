import sys
from flask import Flask, request
from flask_cors import CORS
import pandas as pd
sys.path.append('../database/')
import python_sql_alchemy

app = Flask(__name__)
CORS(app)

@app.route('/api/query', methods=['POST'])
def process():
    request_data = request.get_json()
    print(request_data)
    latitude = request_data['latitude']
    print(latitude)
    data = python_sql_alchemy.get_cities_by_latitude(latitude)
    df = pd.DataFrame(data)
    df.columns = data[0].keys()
    json_data = df.to_json()
    return json_data