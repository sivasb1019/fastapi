from models.parents import Parent

# Define a function to get a parent from the database
def get_parent(filters, db):
     return db.query(Parent).filter_by(**filters).first()