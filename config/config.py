from flask import Flask
from config import config  # Import the config instance

app = Flask(__name__)

# Apply the config to the app
app.config.from_object(config)

# Import your routes and other app-related logic
from app import routes

if __name__ == '__main__':
    app.run(debug=config.DEBUG, port=config.PORT)
