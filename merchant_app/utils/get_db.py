from Database.db_config import SessionLocal2

def get_db():
    try:
        session = SessionLocal2()
        yield session
    finally:
        session.close()
        