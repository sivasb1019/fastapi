from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the database URL from the environment variable
DB_URL = os.getenv("DB_PATH")

# Create an engine for the database connection
engine = create_engine(DB_URL)

# Create a session maker for creating database sessions
# This allows us to manage database transactions and sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define a function to get a database session
# This function can be used as a dependency in your FastAPI routes
def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()