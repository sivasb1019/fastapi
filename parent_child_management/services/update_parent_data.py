import json
from fastapi import HTTPException
from utils.get_parent import get_parent
from utils.save_profile_photo import save_profile_photo

# Define a function to update a parent's data in the database
def update_parent_data(request, profile_photo, current_parent, db):
    try:
        # Convert JSON string to JSON object
        request_data = json.loads(request)

        # Construct filters to find the parent
        filters = {"id": current_parent.parent_id, "email": current_parent.email}

        # Fetch parent data from the database
        parent = get_parent(filters, db)

        if not parent:
            # If parent data is not found, raise a 404 Not Found exception
            raise HTTPException(status_code=404, detail="Parent data not found")

        # Save the profile photo if provided
        if profile_photo:
            parent.profile_photo = save_profile_photo(profile_photo, parent.id)

        # Update parent data fields if values are provided in the request
        parent.firstname = request_data.get("firstname", parent.firstname)
        parent.middlename = request_data.get("middlename", parent.middlename)
        parent.lastname = request_data.get("lastname", parent.lastname)
        parent.age = request_data.get("age", parent.age)
        parent.dob = request_data.get("dob", parent.dob)
        parent.mobile = request_data.get("mobile", parent.mobile)
        parent.address_line_1 = request_data.get("address_line_1", parent.address_line_1)
        parent.address_line_2 = request_data.get("address_line_2", parent.address_line_2)
        parent.city = request_data.get("city", parent.city)
        parent.state = request_data.get("state", parent.state)
        parent.country = request_data.get("country", parent.country)
        parent.pincode = request_data.get("pincode", parent.pincode)

        # Commit changes to the database and refresh parent object
        db.commit()
        db.refresh(parent)

        return parent

    except HTTPException:
        # Reraise HTTPException to propagate the error
        raise

    except Exception as e:
        # If any other exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to update parent data: {str(e)}")

    finally:
        # Close the database session
        db.close()
