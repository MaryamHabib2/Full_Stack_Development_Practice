from flask import Flask #import Flask class from flask module

def create_app():  # Define a function to create and configure the Flask application
    app = Flask(__name__) # Initialize the Flask application
    app.config['SECRET_KEY'] = 'mrym' # Set the secret key for the app

    return app  # Return the configured Flask application instance