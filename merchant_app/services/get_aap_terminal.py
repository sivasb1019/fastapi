from fastapi import HTTPException
from models.AAPTerminal import AAPTerminal
from utils.get_branch import get_branch
import os
from dotenv import load_dotenv

load_dotenv()

def get_aap_terminal(session1, session2):
    BRANCH_ID = os.getenv("BRANCH_ID")
    fld_number = get_branch(BRANCH_ID, session2)
    result = session1.query(AAPTerminal).filter(AAPTerminal.Branch_Id == fld_number).first()
    if not result:
        raise HTTPException(status_code=400, detail="Terminal not found")
    return {"terminal": result.Branch_Id}