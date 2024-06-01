from models.CustomerType import CustomerType


def get_customertype_details(session):
    return session.query(CustomerType).all()