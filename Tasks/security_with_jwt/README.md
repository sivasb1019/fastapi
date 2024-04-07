# User Registration Management API with FastAPI

This project is a robust API for managing user registration, authentication, and profile updates securely. Built with FastAPI, PostgreSQL, and JWT (JSON Web Tokens), it offers a comprehensive solution for modern web applications requiring user management features.

## Features

- **User Registration**: Users can register securely by providing essential details such as username, name, email, and password. The registration process ensures data integrity and security.

- **JWT Authorization**: Authentication is handled using JWT tokens, ensuring secure access to protected routes. Tokens are generated upon successful login and are used for subsequent requests, providing a stateless and secure authentication mechanism.

- **Role-Based Access Control**: Role-based permissions are implemented to manage user access effectively. Users can be assigned roles such as Admin or User, each with specific permissions within the application.

- **Profile Management**: Users can update their profile information, including their name and email address, ensuring accurate user data management.

## Project Structure

- **main.py**: The main entry point of the FastAPI application, defining routes and starting the server.

- **routes.py**: Contains route definitions for user registration, authentication, and profile management.

- **user_services.py**: Implements user-related services such as user creation, profile updates, and activity status management.

- **auth_services.py**: Handles user authentication and JWT token generation.

- **utils.py**: Utility functions including password hashing and token verification.

- **database.py**: Configures the PostgreSQL database connection and provides session management.

- **models.py**: Defines SQLAlchemy models for user data storage.

- **user_schemas.py**: Contains Pydantic schemas for user-related data validation and serialization.

- **auth_schemas.py**: Defines Pydantic schemas for authentication data serialization.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>

2. Install dependecies:

   ```bash
   pip install -r requirements.txt

3. Set up environment variables by creating a '.env' file and providing values for 'DB_PATH', 'SECRET_KEY', 'ALGORITHM', and 'ACCESS_TOKEN_EXPIRE_MINUTES'.

4. Run 'main.py' file

5. Access the API documentation at http://127.0.0.1:8000/docs to explore available endpoints and interact with the application.
