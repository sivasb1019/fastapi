from models.DepositMode import DepositMode


def get_depositmode_details(session):
    return session.query(DepositMode).all()