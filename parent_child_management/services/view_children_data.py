from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.children import Children
from utils.get_parent import get_parent

# Define a function to view a parent's children data
def view_children_data(name, age, dob, created_at, updated_at, current_parent, db: Session):
    try:
        # Fetch the parent data based on the current parent's ID and email
        parent = get_parent({"id": current_parent.parent_id, "email": current_parent.email}, db)
        
        # If the parent data is not found, raise a 404 Not Found exception
        if not parent:
            raise HTTPException(status_code=404, detail="Parent data not found")
        
        # Construct the filters based on the provided query parameters
        filters = {"parent_id": current_parent.parent_id}
        if name is not None:
            filters["name"] = name
        if age is not None:
            filters["age"] = age
        if dob is not None:
            filters["dob"] = dob
        if created_at is not None:
            filters["created_at"] = created_at
        if updated_at is not None:
            filters["updated_at"] = updated_at

        # Fetch the children data based on the filters
        children = db.query(Children).filter_by(**filters).all()

        # If no children data is found, raise a 404 Not Found exception
        if not children:
            raise HTTPException(status_code=404, detail="No data not found")
        return children
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()