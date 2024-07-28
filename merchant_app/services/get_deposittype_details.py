from models.DepositType import DepositType


def get_deposittype_details(session):
    return session.query(DepositType).all()