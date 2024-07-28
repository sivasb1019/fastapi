from models.users import User

# Define a function to get a user from the database
def get_user(filters, db):
     return db.query(User).filter_by(**filters).first()