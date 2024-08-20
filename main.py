from flask import Flask
from app import app
from routes import *


app.register_blueprint(bp_foods)
app.register_blueprint(bp_users)


if __name__ == "__main__":
    app.run()