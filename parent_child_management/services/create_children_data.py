from fastapi import HTTPException

from utils.get_parent import get_parent
from utils.notify_admin import notify_admin
from models.children import Children

# Define a function to create a new child for a parent
def create_children_data(request, background_tasks, current_parent, db):
    try:
        # Fetch the parent data based on the current parent's ID and email
        parent_id = current_parent.parent_id
        parent = get_parent({"id": parent_id, "email": current_parent.email}, db)

        # If the parent is not found, raise a 404 Not Found exception
        if not parent:
            raise HTTPException(status_code=404, detail="Parent not found")
        
        # Create a new child record and add it to the database
        new_child = Children(**request.dict(exclude_unset=True), parent_id=parent_id)
        db.add(new_child)
        db.commit()
        db.refresh(new_child)

        # Add a background task to notify the admin about the new child
        background_tasks.add_task(notify_admin, new_child.name)
        return {"message": f"New children created with id: {new_child.id}"}
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()