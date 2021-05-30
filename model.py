from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__='users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        )
    first_name = db.Column(db.Text)
    username = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)

    favourite_plants= db.relationship("Plant",
                            secondary="favourites",
                            backref="users_who_liked")
                            ##secondary reference connects the plants and users
                            ##tables, we dont want to store lists. Secondary pretends 
                            ##that table doesnt need to exist
    
    def __repr__(self):
    
        return f'<User user_id={self.user_id} email={self.email}>'

class Plant(db.Model):
    """A plant"""

    __tablename__='plants'

    plant_id = db.Column(db.String,
                        primary_key=True)
    name = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        return f'<plant plant_id={self.plant_id}>'

class Favourite(db.Model):
    """A favourited plant"""

    __tablename__='favourites'

    favourite_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    plant_id = db.Column(db.String,
                        db.ForeignKey('plants.plant_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<Liked plant_id={self.plant_id}>'



def connect_to_db(flask_app, db_uri='postgresql:///plants', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)