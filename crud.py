"""CRUD """

from model import db, User, Plant, Favourite, connect_to_db

def create_user(first_name, username, email, password):
    """Create and return a new user"""

    user=User(first_name=first_name, username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()
    
    return user

def verify_user(username, password):
    """verify if user has an account"""
    user=User(username=username, password=password)
    
    db.session.add(user)
    db.session.commit()
    
    return user

def favourite_a_plant(user_id, plant_id):
    liked=Favourite(user_id=user_id, plant_id=plant_id)
    
    db.session.add(liked)
    db.session.commit()

    return liked


if __name__ == '__main__':
    from server import app
    connect_to_db(app)



