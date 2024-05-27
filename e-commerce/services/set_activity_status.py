from fastapi import HTTPException, status

from models.UserTable import UserTable

def set_active_status(user_id, active_status, current_user, db):
    if current_user.role != 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User '{current_user.email}' is unauthorized to modify activity status"
        )
    user = db.query(UserTable).filter(UserTable.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Given id '{user_id}' not found"
        )
    user.is_active = active_status
    db.commit()
    return {"message": f"{user.email} active status is set to {active_status}"}