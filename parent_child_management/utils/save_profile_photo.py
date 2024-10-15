import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
UPLOAD_DIRECTORY = os.getenv("UPLOAD_DIRECTORY")
EXTENSIONS = os.getenv("EXTENSIONS")

def save_profile_photo(file, parent_id):
    try:
        # Create the upload directory if it doesn't exist
        if not os.path.exists(UPLOAD_DIRECTORY):
            os.makedirs(UPLOAD_DIRECTORY)

        # Extract file extension
        extension = file.filename.split('.')[-1]

        # Check if the file extension is allowed
        if extension not in EXTENSIONS:
            raise HTTPException(status_code=400, detail=f"File type not allowed. Allowed extensions: {EXTENSIONS}")

        # Generate a unique filename based on parent_id and extension
        filename = f"{parent_id}.{extension}"
        file_path = os.path.join(UPLOAD_DIRECTORY, filename)

        # Save the file
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        return file_path

    except OSError as e:
        # Handle OS-related errors (e.g., permission denied, file system full)
        raise HTTPException(status_code=500, detail=f"Failed to save profile photo: {str(e)}")

    except Exception as e:
        # Handle other unexpected errors
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
