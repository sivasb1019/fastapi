from models.UserTable import UserTable

def get_user(email, db):
     return db.query(UserTable).filter(UserTable.email == email).first()