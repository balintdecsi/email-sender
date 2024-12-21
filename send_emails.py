import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_addresses):
    from_address = "your_email@example.com"
    password = "your_password"

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_address, password)

    for to_address in to_addresses:
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(from_address, to_address, msg.as_string())

    server.quit()

if __name__ == "__main__":
    subject = "Your Subject Here"
    body = "Your email body here."
    to_addresses = ["recipient1@example.com", "recipient2@example.com"]

    send_email(subject, body, to_addresses)