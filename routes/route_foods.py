from flask import Flask, Blueprint, jsonify, request
import requests


bp_foods = Blueprint('bp_foods', __name__)


@bp_foods.route('/fineli/params', methods=['POST'])
def fineliParams():
    params = request.json
    print(params)

    return '{"msg": "OK"}'

@bp_foods.route('/api/foods/fetch', methods=['GET'])
def fetch_food():
    
    return '{"msg": "OK"}'

@bp_foods.route('/search', methods=['GET', 'POST'])
def search():

    data = request.json

    query = data['name']
    
    params = 'q=' + query

    url = 'https://fineli.fi/fineli/api/v1/foods'

    try:
        response = requests.get(url, params=params)
        
        response.raise_for_status()

        api_data = response.json
        print(api_data)
        return jsonify(api_data)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})


