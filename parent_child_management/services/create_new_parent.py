from fastapi import HTTPException
from schemas.parents_schema import RegisterRequest
from models.parents import Parent
from utils.get_parent import get_parent
from utils.password_auth import hash_password
from utils.send_mail import send_email

def create_new_parent(request:RegisterRequest, db):
    try:
        # Check if the email is already registered
        if get_parent({"email":request.email}, db):
            # If the parent data is found, raise a 400 Bad Request exception
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Hash the provided password
        request.password = hash_password(request.password)
        
        # Create a new Parent instance
        new_parent = Parent(**request.dict())
        
        # Add the new parent to the database
        db.add(new_parent)
        db.commit()
        
        # Prepare the email subject and body for sending account verification link
        email_subject = "Cloudyapps Acount Verification Email"
        email_body = f"""
        <html>
            <body>
                <p>Dear {new_parent.firstname},</p>
                <p>Thank you for choosing Cloudyapps. We're reaching out to provide you with a account verification link for Login. Please proceed with caution and follow the instructions below:</p>
                <!-- Place Link in a box with inline styling -->
                <div style=" padding: 10px; width: fit-content; margin: 0 auto; text-align: center; background-color: #008CBA; border-radius: 5px">
                    <a href="http://127.0.0.1:8000/api/v1/auth/verify-account/?parent_id={new_parent.id}" 
                        style="text-decoration: none; color:#fff">
                    Verify Account
                    </a>
                </div>
                <p><b>Warning:</b></p>
                <p>Verfying your account confirms your identity. Only proceed if you initiated this request. If unsure, contact us immediately.</p>
                <br>
                <p>Sincerely,</p>
                <p>Team Cloudyapps</p>
            </body>
        </html>
        """
        # Send the verification email
        send_email(new_parent.email, email_subject, email_body)
        
        # Refresh the new parent instance to get the updated data
        db.refresh(new_parent)
        
        # Return a success message
        return {"message": "Parent registered successfully. Please check your email for the activation link."}
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()