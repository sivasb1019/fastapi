from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.children import Children
from utils.get_parent import get_parent

# Define a function to update a child's data
def update_children_data(child_id, request, current_parent, db: Session):
    try:
        # Fetch the parent data based on the current parent's ID and email
        parent = get_parent({"id": current_parent.parent_id, "email": current_parent.email}, db)

        # If the parent is not found, raise a 404 Not Found exception
        if not parent:
            raise HTTPException(status_code=404, detail="Parent not found")
        
        # Fetch the child data based on the provided child_id
        child = db.query(Children).filter_by(**{"id": child_id}).first()
        if not child:
            # If the child data is not found, raise a 404 Not Found exception
            raise HTTPException(status_code=404, detail="Child data not found")
        
        # Update the child's data based on the request
        child.name = request.name if request.name else child.name
        child.age = request.age if request.age else child.age
        child.dob = request.dob if request.dob else child.dob

        # Commit the changes to the database and refresh the child data
        db.commit()
        db.refresh(child)
        return child
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()