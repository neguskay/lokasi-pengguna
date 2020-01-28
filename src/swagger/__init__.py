# Imports
from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

# Register Swagger Blueprint
swagger = Blueprint("swagger", __name__)


# Defaults for bp
SWAGGER_PATH = '/swagger'
API_DOCUMENTATION_JSON_PATH = '/static/swagger.json'


# Routes
@swagger.route("/")
def api_documentation():
    return send_from_directory("static", API_DOCUMENTATION_JSON_PATH)


"""
    Some util methods
"""


def get_swagger_bp():
    swagger_bp = get_swaggerui_blueprint(
        SWAGGER_PATH,
        API_DOCUMENTATION_JSON_PATH,
        config={
            'app_name': "DWP API Users Retriever"
        }
    )

    return swagger_bp
