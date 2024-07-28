from fastapi import HTTPException
from models.users import User
from utils.get_user import get_user
from utils.password_auth import hash_password

def create_new_user(request, db):
    try:
        # Check if the email is already registered
        if get_user({"email":request.email}, db):
            # If the user data is found, raise a 400 Bad Request exception
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Hash the provided password
        request.password = hash_password(request.password)
        
        # Create a new user instance
        new_user = User(**request.dict())
        
        # Add the new user to the database
        db.add(new_user)
        db.commit()
                
        # Refresh the new user instance to get the updated data
        db.refresh(new_user)
        
        # Return a success message
        return {"message": "user registered successfully. Please login with your email and password."}
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()