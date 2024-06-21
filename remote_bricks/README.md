# FastAPI MongoDB User Management API

This project implements a FastAPI-based RESTful API for managing user registrations, logins, and linking user IDs using MongoDB as the backend database.

## Features

- **User Registration**: Register new users with email, password, and username.
- **User Login**: Authenticate users with email and password.
- **Linking IDs**: Associate user IDs with other IDs.
- **Data Retrieval**: Fetch user data including linked IDs.
- **User Deletion**: Delete users and associated data across collections.

## Project Structure

The project structure is organized as follows:

- **`main.py`**: Entry point of the FastAPI application, includes routing setup.
- **`schemas/user_schemas.py`**: Pydantic models for data validation.
- **`config/mdb_config.py`**: Configuration file for MongoDB connection setup.
- **`routes/user_controller.py`**: FastAPI router with endpoints for user management.
- **`utils/password_auth.py`**: Utility functions for hashing and verifying passwords.
- **`.env`**: Environment variables file for storing MongoDB credentials.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set up .env file**
   ```bash
   DB_URL=""
   DB_NAME=""
   USERS_COLLECTION=""
   LINKING_COLLECTION=""

4. Run 'main.py' file or Run the application using below code in cmd:

    ```bash
    uvicorn main:app --reload
    ```

5. Access the API documentation at http://127.0.0.1:8000/docs to explore available endpoints and interact with the application.
