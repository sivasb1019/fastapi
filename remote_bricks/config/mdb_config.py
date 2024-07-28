import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

# Load environment variables from .env file
load_dotenv()

# Read MongoDB connection details from environment variables
DB_URL = os.getenv("DB_URL")
DB_NAME = os.getenv("DB_NAME")
USERS_COLLECTION = os.getenv("USERS_COLLECTION")
LINKING_COLLECTION = os.getenv("LINKING_COLLECTION")

# Create MongoDB client and connect to the database
client = MongoClient(DB_URL)
db = client[DB_NAME]

# Access specific collections within the database
users_collection = db[USERS_COLLECTION]
linking_collection = db[LINKING_COLLECTION]
