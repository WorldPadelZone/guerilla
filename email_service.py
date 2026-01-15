import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

class EmailService:
    def __init__(self):
        self.server = config.SMTP_SERVER
        self.port = config.SMTP_PORT
        self.email = config.SENDER_EMAIL
        self.password = config.SENDER_PASSWORD

    def send_email(self, recipient, subject, html_content):
        """
        Sends an email to the recipient.
        If credentials are missing, prints a mock message instead.
        """
        if not self.email or not self.password:
            print(f"\n[MOCK SEND] Credentials not found. Skipping real email.")
            print(f"To: {recipient}")
            print(f"Subject: {subject}")
            print(f"Body (Preview): {html_content[:100]}...")
            print("To send real emails, set GEMAIL_SENDER_EMAIL and GEMAIL_SENDER_PASS environment variables.\n")
            return

        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(html_content, 'html'))

            print(f"Connecting to {self.server}...")
            server = smtplib.SMTP(self.server, self.port)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, recipient, text)
            server.quit()
            print(f"Email sent successfully to {recipient}")
        except Exception as e:
            print(f"Failed to send email: {e}")
