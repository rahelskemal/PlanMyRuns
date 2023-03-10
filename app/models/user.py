from app import db
from app.weekly_miles_calculator import calculate_weekly_goal
from app.route_option_2 import get_points_of_interest

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    desired_start_date = db.Column(db.DateTime)
    goal_date = db.Column(db.DateTime)
    city = db.Column(db.String)
    street = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    state = db.Column(db.String)
    goal = db.Column(db.String(100))


    def user_dict(self):
        return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "email": self.email,
        "password": self.password,
        "desired_start_date": self.desired_start_date,
        "goal_date" : self.goal_date,
        "city" : self.city,
        "street" : self.street,
        "zip_code" : self.zip_code,
        "state" : self.state,
        "weekly_goal": calculate_weekly_goal(self),
        "goal": self.goal
        # "nearby_parks": get_points_of_interest(self)
        
    }

    def return_one_user(self):
        print("return one user is called")
        return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "email": self.email,
        "password": self.password,
        "desired_start_date": self.desired_start_date,
        "goal_date" : self.goal_date,
        "city" : self.city,
        "street" : self.street,
        "zip_code" : self.zip_code,
        "state" : self.state,
        "goal": self.goal,
        "weekly_goal": calculate_weekly_goal(self),
        # "nearby_parks": get_points_of_interest(self)
        }
