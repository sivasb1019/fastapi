from sqlalchemy import MetaData
from Database.db_config import mos_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_id(session):

    BRANCH_ID = os.getenv("BRANCH_ID")
    MERCHANT_ID = os.getenv("MERCHANT_ID")
     
    
    return {"branch_id": BRANCH_ID,
            "merchant_id": MERCHANT_ID}
