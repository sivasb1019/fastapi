from models.BookType import BookType


def get_booktype_info(session):
    return session.query(BookType).all()