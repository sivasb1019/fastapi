from pydantic import BaseModel
from datetime import date

# Define a CreateChildRequest model to handle the creation of a new child
class CreateChildRequest(BaseModel):
    name: str
    age: int
    dob: date

    class Config:
        from_attributes = True

# Define an UpdateChildRequest model to handle updates to a child's information
class UpdateChildRequest(BaseModel):
    name: str | None = None
    age: int | None = None
    dob: date | None = None

    class Config:
        from_attributes = True

class ViewChild(CreateChildRequest):
    id: int