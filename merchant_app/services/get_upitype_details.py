from models.UPIType import UPIType


def get_upitype_details(session):
    return session.query(UPIType).all()