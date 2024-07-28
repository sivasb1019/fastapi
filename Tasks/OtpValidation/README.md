# OTP Validation API

This API is built using FastAPI framework to facilitate OTP (One Time Password) validation for user authentication.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd OtpValidation
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view and interact with the available endpoints.

## API Endpoints

### Generate Token

- **Endpoint:** `/generate-token`
- **Method:** POST
- **Description:** Generates an access token based on provided credentials (email and OTP).
- **Request Body:**
    ```json
    {
        "email": "example@example.com",
        "otp": "123456"
    }
    ```
- **Response:**
    ```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "bearer"
    }
    ```

### User Operations

#### Create User

- **Endpoint:** `/user/create_user`
- **Method:** POST
- **Description:** Creates a new user with provided email and password.
- **Request Body:**
    ```json
    {
        "email": "newuser@example.com",
        "password": "password123"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Success! New user created from email, 'newuser@example.com'"
    }
    ```

#### OTP Generation

- **Endpoint:** `/user/otp_generation`
- **Method:** POST
- **Description:** Generates an OTP (One Time Password) for provided email.
- **Request Body:**
    ```json
    {
        "email": "example@example.com",
        "password": "password123"
    }
    ```
- **Response:**
    ```json
    {
        "message": "OTP generated successfully to 'example@example.com'",
        "time_limit": "OTP time limit is 1 minute"
    }
    ```

#### Update Password

- **Endpoint:** `/user/update_password`
- **Method:** PUT
- **Description:** Updates the password for the authenticated user.
- **Request Body:**
    ```json
    {
        "email": "example@example.com",
        "new_password": "newpassword123"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Password changed successfully for 'example@example.com'"
    }
    ```
