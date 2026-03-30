from nt import environ
from dotenv import load_dotenv
from os import environ

# Load environment variables from the .env file
load_dotenv()

# Access environment variables as if they came from the actual environment
SQLALCHEMY_DATABASE_URI=environ.get('DATABASE_URL')