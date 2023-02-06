from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.user import User
from datetime import datetime


users_bp = Blueprint("users", __name__, url_prefix="/users")


#validate user id
def validate_id(cls, id):
    try: 
        id = int(id)
    except:
        abort(make_response ({"message":f"{cls.__name__} {id} invalid"}, 400))

    obj = cls.query.get(id)

    if not obj:
        abort(make_response({"message":f"{cls.__name__} {id} not found"}, 404))

    return obj


#POST request to create a user at /users

@users_bp.route("", methods=["POST"])
def create_user_profile():
    request_body=request.get_json()
    new_user = User( 
        email = request_body["email"],
        password = request_body["password"],
        first_name = request_body["first_name"],
        last_name = request_body["last_name"],
        desired_start_date = datetime.strptime(request_body["desired_start_date"],"%Y-%m-%d").date(),
        goal_date = datetime.strptime(request_body["goal_date"],"%Y-%m-%d").date(),
        city = request_body["city"],
        street = request_body["street"],
        zip_code = request_body["zip_code"],
        state = request_body["state"],
        goal = request_body["goal"]
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "id": new_user.id,
        "goal":new_user.goal,
        "email": new_user.email,
        "password": new_user.password,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "desired_start_date": new_user.desired_start_date,
        "goal_date" : new_user.goal_date,
        "city" : new_user.city,
        "street" : new_user.street,
        "zip_code" : new_user.zip_code,
        "state" : new_user.state,
    }, 201
    

#GET request to get a list of users at /users
@users_bp.route("", methods=["GET"])
def get_all_users():
    user_list = []

    users=User.query.all()

    for user in users:
        user_list.append(user.user_dict())

    return jsonify(user_list)


#GET request to get data from one user /users/id
    # return should include the calculated weekly mile recs 
    # return should also display weekly routes

@users_bp.route("/<id>", methods=["GET"])

def get_one_user(id):
    user = validate_id(User, id)

    return user.return_one_user() , 200 

#PUT request to replace user data with new data from the request body 

@users_bp.route("/<id>", methods=["PATCH"])

def update_user_start_date(id):
    request_body=request.get_json()
    user = validate_id(User, id)

    if "desired_start_date" in request_body:
        user.desired_start_date = request_body["desired_start_date"]
    if "goal_date" in request_body:
        user.goal_date = request_body["goal_date"]
    if "state" in request_body:
        user.goal_date = request_body["state"]
    if "street" in request_body:
        user.goal_date = request_body["street"]
    if "city" in request_body:
        user.goal_date = request_body["city"]
    if "zip_code" in request_body:
        user.goal_date = request_body["zip_code"]
    if "goal" in request_body:
        user.goal_date = request_body["goal"]

    db.session.commit()
    
    return make_response({"details": f'User {id}: " Profile sucessfully updated'})



#DELETE request to delete a user

@users_bp.route("/<id>", methods=["DELETE"])

def delete_user(id):
    user=validate_id(User, id)
    db.session.delete(user)
    db.session.commit()
    return make_response({"details":f'User ID: {id}: {user.first_name} successfully deleted'})