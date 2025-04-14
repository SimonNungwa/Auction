from flask import Flask
from routes.routes import routes  # Import routes from the routes module

app = Flask(__name__)

# Register the Blueprint with the app
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
