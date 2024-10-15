from datetime import date


from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
from database.orm_setup import get_session

from schemas.parents_schema import ListParent
from schemas.child_schema import CreateChildRequest, UpdateChildRequest, ViewChild
from utils.get_current_parent import get_current_parent
from services.get_parent_data import get_parent_data
from services.update_parent_data import update_parent_data
from services.create_children_data import create_children_data
from services.update_children_data import update_children_data
from services.view_children_data import view_children_data

router = APIRouter()

@router.get("/get-parent", tags=["parent"], response_model=ListParent)
async def get_parent(current_parent: object = Depends(get_current_parent), session: Session = Depends(get_session)):
    return get_parent_data(current_parent, session)

@router.put("/update-parent", tags=["parent"], response_model=ListParent, response_model_exclude_none=True)
async def update_parent(request: str = Form(), profile_photo: UploadFile = File(None),
                        current_parent: object = Depends(get_current_parent), session: Session = Depends(get_session)):
    
    '''
    - Request must be a string in json format, It should be converted into string when frontend made a request.
            
    - {
        "firstname": "string",
        "middlename": "string",
        "lastname": "string",
        "age": 0,
        "dob": "2024-07-15",
        "mobile": "string",
        "address_line_1": "string",
        "address_line_2": "string",
        "city": "string",
        "state": "string",
        "country": "string",
        "pincode": "string"
       }

    - If the converting JSON to string is little bit trouble, we can also send a data as a form from a backend itself.

    - For profile picture nly ["png", "jpg", "jpeg"] these types of picture is valid. We can add more extensions if we want. 
    '''
    return update_parent_data(request, profile_photo, current_parent, session)

@router.post("/create-children", tags=["child"])
async def create_children(request: CreateChildRequest, background_tasks: BackgroundTasks,
                           current_parent: object = Depends(get_current_parent), session: Session = Depends(get_session)):
    return create_children_data(request, background_tasks, current_parent, session)

@router.put("/update-children", tags=["child"], response_model=ViewChild)
async def update_children(child_id: int, request: UpdateChildRequest, current_parent: object = Depends(get_current_parent), session: Session = Depends(get_session)):
    return update_children_data(child_id, request, current_parent, session)

@router.get("/view-children", tags=["child"])
async def view_children(name: str | None = None, age: int | None = None, dob: date | None = None,
                        created_at: date | None = None, updated_at: date | None = None,
                        current_parent: object = Depends(get_current_parent), session: Session = Depends(get_session)):
    return view_children_data(name, age, dob, created_at, updated_at, current_parent, session)


