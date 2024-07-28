from fastapi import status, HTTPException

from utils.get_user import get_user
from models.UserTable import UserTable

def delete_users(user_id, current_user, session):
    if current_user.role != 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid operation: Deleting users are unauthorized for sellers and customers."
        )
    
    try:
        session.query(UserTable).filter(UserTable.user_id == user_id).delete()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
