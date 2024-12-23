from dotenv import dotenv_values
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

env = dotenv_values(".env")

def send_email(subject, body, to_addresses):
    from_address = env["SENDER"]
    password = env["PASSWORD"]

    # Set up the SMTP server using SMTP_SSL and the with statement
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_address, password)

        for to_address in to_addresses:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(from_address, to_address, msg.as_string())

if __name__ == "__main__":
    subject = "Christmas Party"
    body = "This is a test"
    to_addresses = env["RECIPIENTS"].split(",")

    send_email(subject, body, to_addresses)