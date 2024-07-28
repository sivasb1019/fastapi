from sqlalchemy import MetaData
from Database.db_config import mos_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_branch(branch_id, session):

    BRANCH = os.getenv("BRANCH")
    return BRANCH