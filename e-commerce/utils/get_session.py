from databases.db_setup import SessionLocal

def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()