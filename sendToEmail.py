import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, zip_file_path):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    if os.path.isfile(zip_file_path):
        with open(zip_file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(zip_file_path)}")
            message.attach(part)
    else:
        print(f"The provided path {zip_file_path} is not a valid file.")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully with attachment!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()

if len(sys.argv) < 3:
    print(f"Usage: python sendToEmail.py <zip_file_path> <receiver_email>")
    sys.exit(1)

load_dotenv()
sender_email = "lbansal1_be22@thapar.edu"
sender_password = os.getenv("password")
receiver_email = sys.argv[2]
zip_file_path = sys.argv[1]

send_email_with_attachment(sender_email, sender_password, receiver_email, "Attached Zip File", "Please find the attached zip file.", zip_file_path)
