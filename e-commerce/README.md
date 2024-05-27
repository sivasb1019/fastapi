# E-commerce Backend APIs

This project is an e-commerce backend application that provides functionalities for user authentication, product management, and cart handling. It supports role-based access control for Admins, Sellers, and Customers.

## Features

- **User Authentication:**
  - User registration with email verification.
  - Login with OTP authentication and JWT token generation.
  - Password update for authenticated users.

- **Role-based Access Control:**
  - Admins can create new Admins and Sellers.
  - Sellers can add, update, and manage products.
  - Customers can add products to their cart and manage their purchases.

- **Product Management:**
  - Adding new products with optional discount pricing.
  - Updating existing product details.
  - Deleting products.

- **Cart Management:**
  - Adding products to the customer's cart.
  - Ensuring product availability and updating stock accordingly.

## Endpoints

- **User Endpoints:**
  - `POST /signup`: Register a new user.
  - `POST /login`: User login with OTP authentication.
  - `PUT /update_password`: Update user's password.
  
- **Admin Endpoints:**
  - `POST /create_user`: Create new Admins and Sellers.
  - `DELETE /delete_user/{user_id}`: Delete a user.
  - `PUT /set_active_status/{user_id}`: Modify user's active status.

- **Seller Endpoints:**
  - `POST /add_products`: Add new products.
  - `PUT /update_products/{product_id}`: Update existing product details.

- **Customer Endpoints:**
  - `POST /add_cart_products`: Add products to the cart.

## Getting Started

### Prerequisites

- Python 3.x (x - version (e.g., 3.10.6, 3.12.3,...))
- FastAPI
- SQLAlchemy
- JWT
- A database setup (e.g., PostgreSQL, MySQL, SQLite)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-backend.git
   cd ecommerce-backend

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database settings in the project.

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

- Access the API documentation at `http://localhost:8000/docs` for interactive API exploration.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Additional Information
You can create the e-commerce UI (frontend setup) using this backend because it provides a medium-level setup for an e-commerce application.

