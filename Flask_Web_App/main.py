from website import create_app  # Import the create_app function from the website package 

app = create_app()  # Create an instance of the Flask application

if __name__ == '__main__':  # Check if the script is being run directly
    app.run(debug=True)  # Run the Flask application in debug mode