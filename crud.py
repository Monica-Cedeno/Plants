"""CRUD """

from model import db, User, Plant, Favourite, connect_to_db

def create_user(first_name, username, email, password):
    """Create and return a new user"""

    user=User(first_name=first_name, username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()
    
    return user

def verify_user(email, password):
    """verify if user has an account"""
    user=User(email=email, password=password)
    
    db.session.add(user)
    db.session.commit()
    
    return user

def favourite_a_plant(user_id, plant_id):
    liked=Favourite(user_id=user_id, plant_id=plant_id)
    
    db.session.add(liked)
    db.session.commit()

    return liked

def adding_plant(plant_id, name, img_url=None): 
    # TODO: opportunity to optimize: could include this logic inside the favourite_a_plant fn, 
    # use one db.commit for both plan and fav
    plant = Plant(plant_id=plant_id, name=name, img_url=img_url)

    db.session.add(plant)
    db.session.commit()

    return plant 

def get_plants_by_user(user_id):
    

    return User.query.get(user_id).favourite_plants


if __name__ == '__main__':
    from server import app
    connect_to_db(app)



