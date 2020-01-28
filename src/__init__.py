# Imports
from flask import Flask, render_template


# Method to create app
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # Imports for app creation
    from src.api import api
    from src.swagger import get_swagger_bp, SWAGGER_PATH

    # App Blueprints/Routes Initialisation
    app.register_blueprint(api)
    app.register_blueprint(get_swagger_bp(), url_prefix=SWAGGER_PATH)

    # App Routes
    # Html from boiler plate forked
    @app.route('/')
    def home():
        """
            Route: Index/Home
        """
        return render_template('pages/placeholder.home.html')

    @app.route('/about')
    def about():
        """
            Route: About Page.
        """
        return render_template('pages/placeholder.about.html')

    @app.errorhandler(500)
    def internal_error(error):
        """
            Return this page if Internal Server Error.
        """
        # db_session.rollback()
        return render_template('errors/500.html'), 500

    @app.errorhandler(404)
    def not_found_error(error):
        """
            Return this page if Not Found Error.
        """
        return render_template('errors/404.html'), 404

    return app


# Default port: 5000
# Default debug: True, set to False on prod
# Entry point of app
if __name__ == '__main__':
    app = create_app()

    with app.app_context():

        app.run(debug=True, port=5000)
