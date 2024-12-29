import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate OTP
def generate_otp(length=6):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

# Function to send OTP email
def send_otp_email(otp, sender_email, sender_password, recipient_email):
    # Set up the email parameters
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"

    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server (e.g., Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail's SMTP server and port
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the email account

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

# Example usage:
if __name__ == "__main__":
    sender_email = "pk0844675@gmail.com"  # Your email address
    sender_password = "praveenkumar9414"      # Your email password (use app password if 2FA enabled)
    recipient_email = "praveenk9414@gmail.com"  # Recipient's email address

    # Generate the OTP
    otp = generate_otp()

    # Send the OTP to the recipient email
    send_otp_email(otp, sender_email, sender_password, recipient_email)
