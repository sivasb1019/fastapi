import os
from dotenv import load_dotenv
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_otp(receiver_email, otp):
    # Create message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_email
    message['Subject'] = 'Your OTP for Verification'

    # Email body
    body = f'Your OTP for verification is: {otp}'
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    with SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
