# services.py
from models import User
from database import db

def create_user(username):

    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists.")

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()





