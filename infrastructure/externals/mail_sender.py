import base64
import requests

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

class MailSender:
    def __init__(self):
        self.api_key = Config.MAIL_SENDERS_KEY
        self.sender = Config.SMTP_USER

    def send_mail(self, ctx):
        attachments = []
        for file_path in ctx.attachments:
            with open(file_path, "rb") as f:
                attachments.append({
                    "filename": file_path.split("/")[-1],
                    "content": base64.b64encode(f.read()).decode("utf-8"),
                    "disposition": "attachment"
                })

        payload = {
            "from": {"email": self.sender, "name": ctx.from_name},
            "to": [{"email": r} for r in ctx.recipients],
            "subject": ctx.subject,
            "html": ctx.body,
            "attachments": attachments
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        requests.post("https://api.mailersend.com/v1/email", json=payload, headers=headers)

mail_sender = MailSender()