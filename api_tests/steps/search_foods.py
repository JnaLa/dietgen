# This file contains the step definitions for the search_foods.feature file
import requests
import json
from behave import *
import logging
from hamcrest import *


@given('I search for a {search_term}')
def step_impl(context, search_term):
    context.food = search_term
    url = f'{context.base_url}/fineli/search'
    logging.info(f"Search term: {url}")
    headers = {
        'Content-Type': 'application/json'
    }
    data = {'data': search_term}
    logging.info(f"Sending request to {url} with payload: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    context.response = response
    logging.info(f"Received response: {context.response.json()}")
    pass

@when('search should succeed')
def step_impl(context):
    assert_that(context.response.status_code, equal_to(200), "Expected status code 200, but was {}".format(context.response.status_code))
    logging.info("Search succeeded with status code 200")
    pass

@then('content should not be empty')
def step_impl(context):
    assert_that(context.response, is_not(empty()), "Expected non-empty response, but got empty")
    logging.info("Confirmed: Content is not empty")
    pass

@when('I select the food {food_name}')
def step_impl(context, food_name):
    context.food_id = None
    
    for food in context.response.json():
        if food['name'] == food_name:
            context.food_id = food['id']
            logging.info(f"Selected food name: {food_name}")
            logging.info(f"Selected food id: {context.food_id}")
            break
    
    if context.food_id is None:
        logging.error(f"Food with name '{food_name}' not found in the response.")
        logging.error(f"Selected food id: {context.response.json()}")
        
        return
    
    url = 'http://localhost:5000/fineli/food/{}'.format(context.food_id)

    headers = {
        'Content-Type': 'application/json'
    }
    data = {'id': context.food_id}
    logging.info(f"Sending request to {url} with payload: {data}")
    response = requests.get(url, headers=headers, data=json.dumps(data))
    context.response = response
    pass


@then('I should see the food details "{food_name}" "{energy_kcal}" "{carbs}" "{sugar}" "{fat}" "{fat_saturated}" "{protein}"')
def step_impl(context, food_name, energy_kcal, carbs, sugar, fat, fat_saturated, protein):

    energy_kcal = float(energy_kcal)
    carbs = float(carbs)
    sugar = float(sugar)
    fat = float(fat)
    fat_saturated = float(fat_saturated)
    protein = float(protein)
    assert_that(context.response.json()['name']['fi'], equal_to(food_name),
               "Expected food name to be {}, but was {}".format(food_name, context.response.json()['name']['fi']))

    assert_that(context.response.json()['energyKcal'], equal_to(energy_kcal),
                 "Expected energy kcal to be {}, but was {}".format(energy_kcal, context.response.json()['energyKcal']))
    assert_that(context.response.json()['carbohydrate'], equal_to(carbs),
                 "Expected carbs to be {}, but was {}".format(carbs, context.response.json()['carbohydrate']))
    assert_that(context.response.json()['sugar'], equal_to(sugar),
                 "Expected sugar to be {}, but was {}".format(sugar, context.response.json()['sugar']))
    assert_that(context.response.json()['fat'], equal_to(fat),
                 "Expected fat to be {}, but was {}".format(fat, context.response.json()['fat']))
    assert_that(context.response.json()['saturatedFat'], equal_to(fat_saturated),
                 "Expected saturated fat to be {}, but was {}".format(fat_saturated, context.response.json()['saturatedFat']))
    assert_that(context.response.json()['protein'], equal_to(protein),
                 "Expected protein to be {}, but was {}".format(protein, context.response.json()['protein']))
    logging.info(f"Confirmed: Food details match expected values")
    
        
    pass