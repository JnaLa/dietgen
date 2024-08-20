from flask import Blueprint, jsonify, request
import requests


bp_foods = Blueprint('bp_foods', __name__)


@bp_foods.route('/mealtypes', methods=['GET'])
def fetchMealTypes():
    mealTypes = [
    {"id": 1, "name": "Breakfast"},
    {"id": 2, "name": "Brunch"},
    {"id": 3, "name": "Lunch"},
    {"id": 4, "name": "Snack"},
    {"id": 5, "name": "Dinner"},
    {"id": 6, "name": "Supper"},
    {"id": 7, "name": "Drink"},
    {"id": 8, "name": "Else"}
]
    return jsonify(mealTypes)





@bp_foods.route('/fineli/search', methods=['GET', 'POST'])
def search():
    data = request.json
    
    if not data or 'data' not in data:
        return jsonify({'error': 'No name provided'}), 400

    query = data['data']
    
    params = {'q': query}

    url = 'https://fineli.fi/fineli/api/v1/foods'

    headers = {
        'User-Agent': 'Dietgen',
        'Authorization': 'Bearer YOUR_API_KEY'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        api_data = response.json()

        filteredFoods = [{
            'id': food['id'],
            'name': food['name']['fi']
        } for food in api_data]
        
        print(filteredFoods)
        
        return filteredFoods
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500




@bp_foods.route('/fineli/food/<id>', methods=['GET'])
def getFoodData(id):
    food_id = id
    url = "https://fineli.fi/fineli/api/v1/foods/"
    headers = {
        'User-Agent': 'Dietgen',
        'Authorization': 'Bearer YOUR_API_KEY'
    }

    try:
        response = requests.get(url + food_id, headers=headers)
        response.raise_for_status()
        api_data = response.json()

        return api_data
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500





    

    

    return '{"msg": "OK"}'
