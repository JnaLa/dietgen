from app import db
from flask_sqlalchemy import SQLAlchemy
from users import User

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(30), nullable=True)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    # profile_picture = db.Column(db.String(500), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, nickname, age, gender, height, weight, bio):
        self.nickname = nickname
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bio = bio
        # self.profile_picture = profile_picture
    

    def obj_to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "bio": self.bio
        }
