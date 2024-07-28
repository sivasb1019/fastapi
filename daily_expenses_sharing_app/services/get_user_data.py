from fastapi import HTTPException
from utils.get_user import get_user

# Define a function to retrieve a user's data from the database
def get_user_data(current_user, db):
    try:
        # Use the get_user utility function to fetch the user data
        user = get_user({"email": current_user.email}, db)

        # If the user is not found, raise a 404 Not Found exception
        if not user:
            raise HTTPException(status_code=404, detail="user not found")

        return user
    
    except Exception as e:
        # If any other exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to retrieve user data: {str(e)}")
    
    finally:
        # Close the database session
        db.close()
