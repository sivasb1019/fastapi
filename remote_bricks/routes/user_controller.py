from fastapi import APIRouter, HTTPException
from schemas.user_schemas import User, Login, LinkID, JoinResponse
from config.mdb_config import users_collection, linking_collection
from utils.password_auth import hash_password, verify_password

router = APIRouter(prefix="/users")

# Endpoint to register a new user
@router.post("/register")
async def register_user(user_request: User):
    # Check if user with the same email already exists
    user_exists = users_collection.find_one({"email": user_request.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the user's password before storing in the database
    user_request.password = hash_password(user_request.password)
    user_data = user_request.__dict__
    user_data.update({"_id": str(users_collection.count_documents({}))})
    result = users_collection.insert_one(user_data)
    return {"id": str(result.inserted_id)}

# Endpoint for user login
@router.post("/login")
async def login_user(user_login: Login):
    user_exists = users_collection.find_one({"email": user_login.email})
    if not user_exists or not verify_password(user_login.password, user_exists["password"]):
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    
    return {"message": f"Login successful for user '{user_exists['username']}'"}

# Endpoint to link a user ID with another ID
@router.post("/link_id")
async def link_id(linking_id: LinkID):
    user_exists = users_collection.find_one({"_id": linking_id.user_id})
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not found")
    
    linking_collection.insert_one({"user_id": user_exists["_id"],
                                   "linked_id": linking_id.linked_id})
    
    return {"message": f"ID linked successfully with user ID '{user_exists['_id']}'"}

# Endpoint to fetch user data including linked IDs
@router.get("/join_user_data/{user_id}", response_model=JoinResponse)
async def join_user_data(user_id: str):
    user_exists = users_collection.find_one({"_id": user_id})
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Retrieve linked IDs associated with the user
    linked_ids = list(linking_collection.find({"user_id": user_id}))
    user_exists["linked_ids"] = [str(linked_id["linked_id"]) for linked_id in linked_ids]
    return user_exists

# Endpoint to delete a user and associated data
@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": user_id})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete all records in linking_collection associated with the user ID
    linking_collection.delete_many({"user_id": user_id})
    
    return {"message": "User and all associated data across collections deleted successfully"}
