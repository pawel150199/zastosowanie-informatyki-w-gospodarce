from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import smtplib
import ssl
from email.message import EmailMessage
from jose import jwt 

from src.core.settings import settings


def send_email(
    email_to: str,
    subject: str,
    body: str,
) -> None:
    assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
    
    sender = settings.EMAILS_FROM_EMAIL
    em = EmailMessage()
    em["From"] = sender
    em['To'] = email_to
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT, context=context) as smtp:
        smtp.login(sender, settings.SMTP_PASSWORD)
        smtp.sendmail(sender, email_to, em.as_string())




def send_test_email(email_to: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    body = f"""
        Hi,

        This is test only

        Best Regards,
        {project_name} team
    """

    send_email(
        email_to=email_to,
        subject=subject,
        body=body
    )


def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    server_host = settings.SERVER_HOST
    link = f"{server_host}/reset-password?token={token}"

    body = f"""
        Hi,

        Here is link to password recovery: {link}.
        It is valid for {settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS} hours.

        Best Regards,

        {project_name} team
    """

    send_email(
        email_to=email_to,
        subject_template=subject,
        body=body
    )


def send_new_account_email(email_to: str, username: str, password: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    link = settings.SERVER_HOST

    body = f"""
        Hi {username},

        Now you have account in our application {project_name}.
        We are hope you will enjoy using our application.

        Your temporary password: {password}

        Best Regards,

        {project_name} team
    """

    send_email(
        email_to=email_to,
        subject_template=subject,
        body=body
    )


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm=settings.ALGORITHM,
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(decoded_token["sub"])
        return decoded_token["sub"]
    except jwt.JWTError:
        return None