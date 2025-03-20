from app import app
from config.config import config

 
if __name__ == '__main__':
    app.run(debug=config.DEBUG, port=config.PORT)

# TODO: Import config file variables 