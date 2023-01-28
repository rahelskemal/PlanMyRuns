import requests
from dotenv import load_dotenv
import os
from app.weekly_miles_calculator import calculate_weekly_goal
import datetime

load_dotenv()

api_key = os.environ.get('API_KEY') 

#query into database to get user location infomation 
def get_lat_and_lon_of_location(user_info):
    street_address = user_info.street 
    user_city = user_info.city
    user_state = user_info.state
    address = f'{street_address},{user_city},{user_state}' 
    
    #use geocoding API to get the  lat and long to pass it into the 
    lat_lon_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(lat_lon_url)

    data = response.json()

    # extract the latitude and longitude from the response
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    location = f"{latitude},{longitude}"

    return location

    # pass location in the places API request

def get_points_of_interest(user_info):
    print("in get point of interest")
    user_location = get_lat_and_lon_of_location(user_info)
    query = "park"
    weekly_miles = calculate_weekly_goal(user_info)
    radius_list = []
    # 1.6 * calculate_weekly_goal(user_info) #change this to km
    #iterate through the list and 
    for r in weekly_miles:
        r = r * 1.6
        radius_list.append(r)
    
    parks_within_range = []
    for i in radius_list:
        radius = i
        place_of_interest_url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={user_location}&radius={radius}&key={api_key}'
        response = requests.get(place_of_interest_url)

        # parse the response as json
        data = response.json()
        for place in data["results"]:
            parks_within_range.append(place["name"])

    #iterate through the results
    
    # for place in data['results']:
    #     parks_within_range.append(place['name'])
    return parks_within_range