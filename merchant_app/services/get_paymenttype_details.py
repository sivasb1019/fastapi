from models.PaymentType import PaymentType


def get_paymenttype_details(session):
    return session.query(PaymentType).all()