from dotenv import load_dotenv
import  os

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi.exceptions import HTTPException


# Load environment variables for the SMTP server
load_dotenv(override=True)
HOST = os.getenv('SMTP_HOST')
PORT = os.getenv('SMTP_PORT')
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")


# Define a function to send an email

def send_email(receiver_email, subject, content_to_be_sent):
    try:
        # Create a MIMEMultipart message
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = SENDER_EMAIL
        message['To'] = receiver_email

        # Create a MIMEText object with HTML content
        html_content = MIMEText(content_to_be_sent, 'html')
        message.attach(html_content)

        # Connect to the SMTP server and send the email
        with SMTP(HOST, PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
            server.quit()
        return {"message": "Mail sent"}
    
    # If there's an error sending the email, raise a 400 Bad Request exception
    except Exception as e:

        raise HTTPException(status_code=400, detail='Not able to send email')



