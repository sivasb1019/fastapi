import os
from dotenv import load_dotenv
import asyncio
from utils.send_mail import send_email

# Load environment variables from the .env file
load_dotenv()
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

# Ensure WAIT_TIME is correctly converted to an integer and handle the default value.

# Define an asynchronous function to notify the admin about a new child
async def notify_user(sender_name, receiver_name, receiver_email):
    
    # Prepare the email subject and body for sending account verification link
    email_subject = "Convin - Expenses Assigned"
    email_body = f"""
    <html>
        <body>
            <p>Dear {receiver_name},</p>
            <p>New expenses are assigned to you by {sender_name}. For more details, please login and check in your account</p>
            <!-- Place Link in a box with inline styling -->
            <div style=" padding: 10px; width: fit-content; margin: 0 auto; text-align: center; background-color: #008CBA; border-radius: 5px">
                <a href="http://127.0.0.1:8000/api/v1/user/user/login-user" 
                    style="text-decoration: none; color:#fff">
                Login Now
                </a>
            </div>
            <p><b>Warning:</b></p>
            <p>If there is any issues regarding the expense assigned or if you are unsure, contact us immediately.</p>
            <br>
            <p>Sincerely,</p>
            <p>Team Convin</p>
        </body>
    </html>
    """

    # Asynchronous background task to notify admin about a new child being added after 5 minutes.
    await asyncio.sleep(300)  # Delay for 300 seconds
    send_email(receiver_email, email_subject, email_body)
