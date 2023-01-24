from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.user import User


users_bp = Blueprint("users", __name__, url_prefix="/users")

#POST request to create a user at /users/user_id

#GET request to get a list of users at /users

#GET request to get data from one user 
    # return should include the calculated weekly mile recs 
    # return should also display weekly routes


#PUT request to replace user data with new data from the request body 

#DELETE request to delete a user

