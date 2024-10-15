# Parent-Child Management Application

## Overview
This project is a Parent-Child Management Application built using FastAPI, PostgreSQL, and SQLAlchemy. The application allows parents to register, manage their profiles, and add child information.

## Technical Requirements
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy

## Functional Requirements
1. **Parent Registration and Account Activation**
   - The application allows parents to register by providing necessary details such as email and password.
   - After registration, the system sends an email containing an activation link to the provided email address.

2. **Parent Login**
   - The application provides an endpoint for parent login using email and password.
   - Upon successful authentication, the parent can access their account and other secured endpoints.

3. **Parent Profile Management**
   - The application allows parents to update their profile information, such as their personal details and profile photo.
   - The profile photo can be uploaded and stored appropriately.

4. **Child Management**
   - The application provides endpoints for creating, updating, and retrieving child information.
   - Each child is linked to the parent in the database.
   - After adding a child, the system sends an email notification to the admin after 5 minutes.

## Additional Requirements
- **Authentication and Authorization**: Implemented using JWT tokens.
- **Validation and Error Handling**: Implemented for all inputs.
- **Environment Variables**: Used for sensitive configurations (e.g., database connection strings, email server settings).
- **Unit Tests**: Provided for the API endpoints.

## Installation and Setup
To run the project locally, follow these steps:
1. Install the dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with the necessary environment variables (e.g., database connection string, email server settings).
3. Run the application: `uvicorn main:app --reload`

## API Endpoints
The application provides the following API endpoints:
- **Parent Registration**: `POST /api/v1/auth/register`
- **Parent Login**: `POST /api/v1/auth/login`
- **Parent Profile Management**: `GET /api/v1/parent/get-parent`, `PUT /api/v1/parent/update-parent`
- **Child Management**: `POST /api/v1/child/create-children`, `PUT /api/v1/child/update-children`, `GET /api/v1/child/view-children`

## Contact
If you have any questions or need assistance, please contact [sivabalanv0810@gmail.com](mailto:sivabalanv0810@gmail.com).

## Acknowledgments
Special thanks to [CloudyApps]() for giving this stunning project.

## Contributors
The following people have contributed to this project:
- [Siva Balan V](https://www.linkedin.com/in/sivabalanv10/)
