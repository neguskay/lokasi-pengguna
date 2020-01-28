from flask import Blueprint, current_app
from flask_restplus import Api
from src.api.v1.people import people_namespace

# Create API blueprint
api = Blueprint("api", __name__, url_prefix="/api/v1")

# Create parent API class
api_routes = Api(api, version="v1")

# Add sub API name-spaces/routes
api_routes.add_namespace(people_namespace, "/people")
