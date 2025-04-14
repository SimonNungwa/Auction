import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = os.getenv('DEBUG', 'TRUE').lower() in ['true', '1']
    PORT = int(os.getenv('PORT', 2024))


config = Config()
