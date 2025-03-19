from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/run/<watermark_id>', methods=['GET'])
def track(watermark_id):
    ip_address = request.remote_addr
    send_email(ip_address, watermark_id)
    return "Tracking successful!"

def send_email(ip_address, watermark_id):
    subject = "Document Access Alert"
    body = f"The document was accessed on device with IP: {ip_address} and watermark ID: {watermark_id}"
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = 'thobekam424@gmail.com'  # Your actual Gmail address
    message['To'] = 'thobekam424@gmail.com'  # Recipient email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Correct SMTP server
            server.starttls()
            server.login('thobekam424@gmail.com', 'gjeqijmtkjfygyvt')  # Use an App Password
            server.sendmail('thobekam424@gmail.com', 'thobekam424@gmail.com', message.as_string())
        print("Email notification sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
