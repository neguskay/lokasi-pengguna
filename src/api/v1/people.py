# Imports
from flask import request
from flask_restplus import Namespace, Resource
from src.models import Users

# Initialise/Create namespace
people_namespace = Namespace("people", description="Endpoint to retrieve list of people")

# Initialise Users globally: eliminate need for multiple calls to API
users_class = Users()

# Global Variables
DEFAULT_API_ENDPOINT = "https://bpdts-test-app.herokuapp.com/city/%s/users"
DEFAULT_LONDON_COORDINATES = {
        "lat": 51.50722,
        "long": 0.1278
    }
DEFAULT_MILES_RANGE = 50


# Routes/Resources
@people_namespace.route("")
class UserList(Resource):
    def get(self):
        users_list_all = users_class.get_users_db()

        if users_list_all:
            response = {
                "success": True,
                "data": users_list_all
            }
            response_code = 200

        else:
            response = {
                "success": False,
                "data": None
            }
            response_code = 400

        return response, response_code


@people_namespace.route("/by-id")
class UserListById(Resource):
    def get(self):
        id = request.args.get("id")

        response = {
            "success": False,
            "data": None
        }
        response_code = 400

        if (id is not None) or (id != ""):
            user = users_class.get_by_id(id=int(id))

            if user:
                response["success"] = True
                response["data"] = user
                response_code = 200

        # return Users().get_users_within_range(miles_range=20, reference_coordinate=DEFAULT_LONDON_COORDINATES)
        return response, response_code


@people_namespace.route("/by-city")
class UserListByCity(Resource):
    users = Users().users_db

    def get(self):
        city = request.args.get("city")

        response = {
            "success": False,
            "data": None
        }
        response_code = 400

        if (city is not None) or (city != ""):
            users_by_city = users_class.get_users_by_city(city=city)

            if users_by_city:
                response["success"] = True
                response["data"] = users_by_city
                response_code = 200
            # external_response = get(url=DEFAULT_API_ENDPOINT % city)
            # print(external_response)
            # print(external_response.url)
            # print(external_response.json())
            # # print(external_response.data)
            # return external_response.json()

        return response, response_code


@people_namespace.route("/by-city-miles")
class UserListByCityWithinMiles(Resource):
    def get(self):
        miles_range = request.args.get("miles")
        ref_lat = request.args.get("latitude")
        ref_long = request.args.get("longitude")

        response = {
            "success": False,
            "data": None
        }
        response_code = 400

        # Check and set miles default
        # # Ref Miles Range
        if (miles_range is None) or (miles_range == ""):
            miles_range = DEFAULT_MILES_RANGE

        # # Ref Coordinates
        if (ref_lat is not None) and (ref_lat != "") and (ref_long is not None) and (ref_long != ""):
            ref_coordinates = {
                "lat": float(ref_lat),
                "long": float(ref_long)
            }
        else:
            ref_coordinates = DEFAULT_LONDON_COORDINATES

        users_by_city_miles = users_class.get_users_within_range(
            miles_range=float(miles_range),
            reference_coordinate=ref_coordinates
        )

        if users_by_city_miles:
            response["success"] = True
            response["data"] = users_by_city_miles
            response_code = 200

        return response, response_code
