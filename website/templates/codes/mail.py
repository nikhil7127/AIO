import smtplib
from email.message import EmailMessage
import imghdr


def sendEmail(sender, receiver, message_details, attachments=None):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    count=0
    server.login(sender[0], sender[1])
    msg = EmailMessage()
    msg["Subject"] = message_details["subject"]
    msg["From"] = sender[0]
    msg.set_content(message_details["message"])
    msg["To"] = receiver
    if attachments:
        for file in attachments:
            try:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
            except Exception:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
    server.send_message(msg)
    server.quit()
    return "Done"

