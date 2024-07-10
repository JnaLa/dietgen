from flask import Flask
from app import app
from routes.route_foods import bp_foods


app.register_blueprint(bp_foods)


if __name__ == "__main__":
    app.run()