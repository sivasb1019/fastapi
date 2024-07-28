from Database.db_config import SessionLocal1

def get_session():
    try:
        session = SessionLocal1()
        yield session
    finally:
        session.close()