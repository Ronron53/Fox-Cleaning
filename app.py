from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")

@app.route("/")
def index():
    return render_template("index.html")

from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/enquiry", methods=["POST"])
def enquiry():
    name = request.form.get("name", "")
    phone = request.form.get("phone", "")
    email = request.form.get("email", "")
    clean_type = request.form.get("clean_type", "")
    details = request.form.get("details", "")
    preferred_date = request.form.get("preferred_date", "")
    message = request.form.get("message", "")

    body = f"""
New Fox Cleaning enquiry

Name: {name}
Phone: {phone}
Email: {email}

Type of clean: {clean_type}
Property / business details: {details}
Preferred start date: {preferred_date}

Message:
{message}
"""

    msg = EmailMessage()
    msg["Subject"] = "New Fox Cleaning enquiry"
    msg["From"] = os.environ.get("EMAIL_USER")
    msg["To"] = os.environ.get("ENQUIRY_TO")
    msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.zoho.com", 587, timeout=10) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
            smtp.send_message(msg)

    except Exception as e:
        print("EMAIL SEND ERROR:", repr(e))
        return """
        <h1>Enquiry could not be sent</h1>
        <p>Please call Fox Cleaning directly on 07986740303.</p>
        <p>Or email hello@foxcleaningherts.co.uk.</p>
        """, 500

    return redirect("/?enquiry=success#contact")


if __name__ == "__main__":
    app.run(debug=True)