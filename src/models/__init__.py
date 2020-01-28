# Imports
from requests import get
from math import sin, cos, sqrt, atan2, radians
from geopy import distance

# Some default variables
DEFAULT_USERS_CITY_ENDPOINT = "https://bpdts-test-app.herokuapp.com/city/%s/users"
DEFAULT_USERS_ENDPOINT = "https://bpdts-test-app.herokuapp.com/users"


# Users Class object
# Called and initialised once with one API to reduce number of calls
class Users(object):
    users_db = None

    def __init__(self):
        self.users_db = get(url=DEFAULT_USERS_ENDPOINT).json()

    def get_users_db(self):
        return self.users_db

    def get_by_id(self, id):
        for user in self.users_db:
            if user["id"] == id:
                return user
        return "Not found User"

    def get_users_within_range(self, miles_range, reference_coordinate):
        users_to_return = []

        for user in self.users_db:

            p1 = {
                "long": float(user["longitude"]),
                "lat": float(user["latitude"])
            }

            dist = calculate_distance_hard_way(p1=p1, p2=reference_coordinate)
            # dist = calculate_distance_geopy(p1=p1, p2=reference_coordinate)

            if dist < miles_range:
                users_to_return.append(user)

        return users_to_return

    def get_users_by_city(self, city):
        users_by_city = get(url=DEFAULT_USERS_CITY_ENDPOINT % city).json()

        return users_by_city


"""
    Some util methods
"""


# Method to calculate distance between two points
def calculate_distance_hard_way(p1, p2):
    # earth radius of earth in km
    earth_radius = 6373.0

    lat1 = radians(p1["lat"])
    lon1 = radians(p1["long"])
    lat2 = radians(p2["lat"])
    lon2 = radians(p2["long"])

    d_longitude = lon2 - lon1
    d_latitude = lat2 - lat1

    a = sin(d_latitude / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_longitude / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    dist = earth_radius * c

    # convert to miles
    conv_fac = 0.621371
    dist_in_miles = dist * conv_fac
    print("Result:", dist_in_miles)

    return dist_in_miles


# Method to calculate distance between two points with 'geopy' external pkg
def calculate_distance_geopy(p1, p2):
    # tuple has to be (<lat>, <long>) for each point to allow geopy to work
    coord_1 = (p1["lat"], p1["long"])
    coord_2 = (p2["lat"], p2["long"])

    dist = distance.distance(coord_1, coord_2).miles
    print("distance result : ", dist)

    return dist
