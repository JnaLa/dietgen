from behave import given, when, then
import requests
import logging

@given('I have the following user')
def step_given_user(context):
    context.user = {
        "email": context.table[0]['email'],
        "password": context.table[0]['password']
    }

@when('I login with "{email}" and "{password}"')
def step_when_login(context, email, password):
    response = requests.post('http://127.0.0.1:5000/users/login', json={
        "email": email,
        "password": password
    })
    context.response = response
    print('Response: ', context.response)

@then('I should get a jwt token')
def step_then_jwt_token(context):
    assert context.response.status_code == 200
    assert 'access_token' in context.response.json()