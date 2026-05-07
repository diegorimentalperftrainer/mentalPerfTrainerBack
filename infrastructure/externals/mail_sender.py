import smtplib
from email.message import EmailMessage
from application.constants import error

from config import Config


class MailContext:
    def __init__(self, subject, recipients, body, from_name, attachments=None):
        self.subject = subject
        self.recipients = self._normalize_recipients(recipients)
        self.body = body
        self.from_name = from_name
        self.attachments = self._normalize_attachments(attachments)

    @staticmethod
    def _normalize_recipients(recipients):
        if isinstance(recipients, str):
            return [recipients]
        elif isinstance(recipients, list):
            return recipients
        else:
            raise TypeError(error.RECIPIENT_ERROR)

    @staticmethod
    def _normalize_attachments(attachments):
        if attachments is None:
            return []
        if isinstance(attachments, str):
            return [attachments]
        if isinstance(attachments, list):
            return attachments
        raise TypeError(error.ATTACHMENT_ERROR)


def send_mail(ctx):
    if not ctx.recipients:
        raise ValueError(error.EMPTY_RECIPIENT_ERROR)

    msg = EmailMessage()
    msg["Subject"] = ctx.subject
    msg["From"] = ctx.from_name
    msg["To"] = ", ".join(ctx.recipients)

    msg.set_content(ctx.body)

    for file_path in ctx.attachments:
        with open(file_path, "rb") as f:
            file_data = f.read()
            file_name = file_path.split("/")[-1]

        msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

    with smtplib.SMTP_SSL(Config.SMTP_HOST, Config.SMTP_PORT) as smtp:
        smtp.login(Config.SMTP_USER, Config.SMTP_PASSWORD)
        smtp.send_message(msg)