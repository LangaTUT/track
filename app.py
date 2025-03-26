from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/run/<watermark_id>', methods=['GET'])
def track(watermark_id):
    ip_address = request.remote_addr
    send_email(ip_address, watermark_id)
    return "Tracking successful!"
# ejxm zmlb ghkc yasv
import os
from dotenv import load_dotenv
load_dotenv()

def send_email(ip_address, watermark_id):
    subject = "Document Access Alert"
    body = f"The document was accessed on device with IP: {ip_address} and watermark ID: {watermark_id}"
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = os.getenv("EMAIL_ADDRESS")  # Use environment variable
    message['To'] = os.getenv("EMAIL_ADDRESS")    # Send to yourself

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))  # Use environment variables
            server.sendmail(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_ADDRESS"), message.as_string())
        print("Email notification sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
