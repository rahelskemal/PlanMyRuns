from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session 
from app import db
import datetime
from dotenv import load_dotenv
# from app.models.user import User 



def calculate_weekly_goal(user_info: int) -> list[int]:
    if type(user_info) == str:
        raise ValueError("input must be an integer")
    # user_info = User.query.get(id)
    goal_date = user_info.goal_date
    start_date = user_info.desired_start_date
    # Define the total mileage goal for a half-marathon
    goal_distance = 13.1 

    #round to the nearest 1 or 2
    # Calculate the number of weeks until the goal date
    weeks_until_goal = (goal_date - start_date).days / 7
    weeks_to_goal = int(weeks_until_goal)
    #if the weeks until goal is more than 16 and less than 8 raise error
    
    # goal_distance = 26.2
    
    # Define the starting weekly mileage goal
    current_weekly_mileage = 4 
    max_weekly_goal = goal_distance * 2

    # Define the increment per week
    increment_per_week = int(max_weekly_goal - current_weekly_mileage)/weeks_to_goal
    weekly_goal_list = []
    
    # Calculate the weekly mileage goal and return list of goals

    first_time = True

    if weeks_to_goal < 8 or weeks_to_goal > 16:
        raise ValueError("Your training must be between 8-16 weeks")
    else:
        # while current_weekly_mileage <= max_weekly_goal and week <= weeks_to_goal:
        for _ in range(weeks_to_goal):
            if current_weekly_mileage < max_weekly_goal:
                if first_time:
                    first_time = False
                else:
                    current_weekly_mileage += increment_per_week
                    rcurrent_weekly_mileage = round(current_weekly_mileage/10)*10
                    
                weekly_goal_list.append(rcurrent_weekly_mileage)
                
        return weekly_goal_list

    """
    calculate how many weeks we have until the goal date
    if the weeks are less than 8 or greater than 16 give error 
    otherwise, proceed 
    
    starting miles is going to be 1/3 of goal 
    initialize a weekly_goal_dict = {}
    
    week = 0
    for i in range(weeks_until_goal)
        week += 1
    
    max_weekly_goal = mile_goal * 2
    until we reach the max_weekly_goal we will:

        weekly_goal_dict["week {week}"] = current_weekly_miles + increment_per_week
        increment the week by 1
        increment the weekly mile goal by the calculation (current_weekly_miles + increment_per_week)

    """

