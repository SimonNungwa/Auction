from app import app
from config.config import config
from auth import auth

 
if __name__ == '__main__':
    app.run(debug=config.DEBUG, port=config.PORT)

