from models.DayInfo import DayInfo


def get_day_info(session):
    return session.query(DayInfo).all()