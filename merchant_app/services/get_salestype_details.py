from models.SalesType import SalesType


def get_salestype_details(session):
    return session.query(SalesType).all()