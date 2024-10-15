from fastapi import HTTPException
from sqlalchemy.orm import Session
from utils.get_parent import get_parent

def account_verification(parent_id, db: Session):
    try:
        # Use the get_parent utility function to fetch the parent data by ID
        parent = get_parent({"id": parent_id}, db)
        # If the parent data is not found, raise a 404 Not Found exception
        if not parent:
            raise HTTPException(status_code=404, detail="Parent not found")
        print(parent.is_active)
        
        # Activate the parent's account
        parent.is_active = True
        print(parent.is_active)
        
        # Commit the changes to the database
        db.commit()
        db.refresh(parent)
        
        # Return a success message
        return {"message": "Account activated successfully."}

    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        # Close the database session
        db.close()
