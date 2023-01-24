from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    desired_start_date = db.Column(db.DateTime)
    mile_goal = db.Column(db.Integer)
    goal_date = db.Column(db.DateTime)
    city = db.Column(db.String)
    street = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    state = db.Column(db.String)

