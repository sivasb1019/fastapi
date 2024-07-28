# Daily Expenses Sharing Application

## Description
The Daily Expenses Sharing Application is a web-based platform designed to help users manage their daily expenses efficiently. Users can add expenses, split them among participants using various methods (equal, exact, percentage), and generate downloadable balance sheets. This application aims to simplify expense tracking and sharing among friends, family, or colleagues.

## Features
- User registration and authentication with JWT tokens.
- Create and manage expenses with detailed descriptions.
- Split expenses using three methods: equal, exact amounts, and percentages.
- View individual and overall expenses.
- Generate and download balance sheets in Excel format.

## Installation Instructions

### Prerequisites
- Python 3.9 or higher
- PostgreSQL database
- Required Python libraries (listed in `requirements.txt`)
- Alembic for database migrations

### Steps to Clone the Repository and Install Dependencies
1. Clone the repository:
   ```bash
   git clone https://github.com/sivasb1019/daily_expenses_sharing_app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd daily-expenses-sharing-app
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Install Alembic:
   ```bash
   pip install alembic
   ```

## Environment Variables
Create a `.env` file in the project root directory with the following variables:

```
DB_PATH=postgresql://username:password@host:port/database_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=20
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
ADMIN_EMAIL=admin@example.com
SENDER_EMAIL=sender@example.com
SENDER_PASSWORD=your_email_password
```

- **DB_PATH**: Connection URL for your PostgreSQL database.
- **SECRET_KEY**: Secret key used for encoding JWT tokens.
- **ALGORITHM**: Algorithm used for JWT token encoding.
- **ACCESS_TOKEN_EXPIRE_MINUTES**: Expiration time for access tokens.
- **SMTP_HOST**: SMTP server for sending emails.
- **SMTP_PORT**: Port for the SMTP server.
- **ADMIN_EMAIL**: Email address for admin notifications.
- **SENDER_EMAIL**: Email address used to send notifications.
- **SENDER_PASSWORD**: Password for the sender email account.

## Database Migrations

### Initial Setup
1. Navigate to the Alembic directory:
   ```bash
   cd alembic
   ```

2. Initialize Alembic (if not already initialized):
   ```bash
   alembic init alembic
   ```

3. Edit the `alembic.ini` file to set your database URL:
   ```ini
   sqlalchemy.url = postgresql://username:password@host:port/database_name
   ```

### Creating Migrations
To create a new migration after making changes to your models:
```bash
alembic revision --autogenerate -m "description_of_changes"
```

### Applying Migrations
To apply the migrations to your database:
```bash
alembic upgrade head
```

### Downgrading Migrations
To downgrade to a previous migration:
```bash
alembic downgrade <revision_id>
```

## Usage Instructions

### How to Run the Application
Start the application using Uvicorn:
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

### Example API Requests
Here are some example requests you can use with `curl` or Postman:

1. **Create a new user**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/api/v1/user/create-user" \
   -H "Content-Type: application/json" \
   -d '{"email": "userdemo@gmail.com", "password": "123456", "name": "Demo User", "mobile": "9876543210"}'
   ```

2. **Login a user**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/api/v1/user/login-user" \
   -H "Content-Type: application/json" \
   -d '{"email": "userdemo@gmail.com", "password": "123456"}'
   ```

3. **Create a new expense**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/api/v1/expenses/create-expenses" \
   -H "Authorization: Bearer your_jwt_token" \
   -H "Content-Type: application/json" \
   -d '{"description": "Dinner", "amount": 100, "split_method": "equal", "splits": [{"user_id": 1}, {"user_id": 2}]}'
   ```

4. **Download balance sheet**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/api/v1/expenses/download-balancesheet?request=Individual Expenses" \
   -H "Authorization: Bearer your_jwt_token" \
   -o balance_sheet.xlsx
   ```

## Testing Instructions
To run the tests, ensure you have pytest installed, then run:
```bash
pytest
```

## Contributing
If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.


## Conclusion
The Daily Expenses Sharing Application is designed to simplify expense management and sharing. With user-friendly features and robust functionality, it aims to make tracking expenses easier for everyone. For any questions or suggestions, feel free to reach out at [sivabalanv0810@gmail.com](sivabalanv0810@gmail.com).
