from fastapi import HTTPException
from utils.get_parent import get_parent

# Define a function to retrieve a parent's data from the database
def get_parent_data(current_parent, db):
    try:
        # Use the get_parent utility function to fetch the parent data
        parent = get_parent({"email": current_parent.email}, db)

        # If the parent is not found, raise a 404 Not Found exception
        if not parent:
            raise HTTPException(status_code=404, detail="Parent not found")
        else:
            parent.profile_photo = None  # Set to None if profile photo does not exist

        return parent
    
    except Exception as e:
        # If any other exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to retrieve parent data: {str(e)}")
    
    finally:
        # Close the database session
        db.close()
