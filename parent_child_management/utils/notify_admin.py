import os
from dotenv import load_dotenv
import asyncio
from utils.send_mail import send_email

# Load environment variables from the .env file
load_dotenv()
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
WAIT_TIME = os.getenv("WAIT_TIME")

# Ensure WAIT_TIME is correctly converted to an integer and handle the default value.
WAIT_TIME = int(WAIT_TIME) if WAIT_TIME and WAIT_TIME.isdigit() else 300

# Define an asynchronous function to notify the admin about a new child
async def notify_admin(child: str):
    # Asynchronous background task to notify admin about a new child being added after 5 minutes.
    await asyncio.sleep(WAIT_TIME)  # Delay for 300 seconds
    send_email(ADMIN_EMAIL, "New Child Added", f"<h3>A new child has been added named, {child}.</h3>")