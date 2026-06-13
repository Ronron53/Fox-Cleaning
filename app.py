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
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["ENQUIRY_TO"]
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.zoho.eu", 465) as smtp:
        smtp.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        smtp.send_message(msg)

    return redirect("/?enquiry=success#contact")

@app.route("/enquiry", methods=["POST"])
def enquiry():
    name     = request.form.get("name", "").strip()
    phone    = request.form.get("phone", "").strip()
    email    = request.form.get("email", "").strip()
    clean    = request.form.get("clean_type", "").strip()
    details  = request.form.get("details", "").strip()
    date     = request.form.get("preferred_date", "").strip()
    message  = request.form.get("message", "").strip()

    # -- Basic validation --
    if not name or not phone:
        flash("Please fill in your name and phone number.", "error")
        return redirect(url_for("index") + "#contact")

    # -- Optional: send yourself an email notification --
    # Uncomment and configure SMTP env vars when ready:
    #
    # try:
    #     body = f"""New enquiry from Fox Cleaning website
    #
    # Name:    {name}
    # Phone:   {phone}
    # Email:   {email}
    # Service: {clean}
    # Details: {details}
    # Date:    {date}
    # Message: {message}
    # """
    #     msg = MIMEText(body)
    #     msg["Subject"] = f"New cleaning enquiry — {name}"
    #     msg["From"]    = os.environ["SMTP_FROM"]
    #     msg["To"]      = os.environ["SMTP_TO"]
    #     with smtplib.SMTP_SSL(os.environ["SMTP_HOST"], 465) as s:
    #         s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
    #         s.send_message(msg)
    # except Exception as e:
    #     print(f"Email error: {e}")

    flash("Thanks — we'll be in touch shortly.", "success")
    return redirect(url_for("index") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)