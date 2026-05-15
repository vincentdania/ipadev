from django.conf import settings
from django.core.mail import send_mail

from config.celery import app


@app.task
def send_contact_notification(submission_id):
    from .models import ContactSubmission

    submission = ContactSubmission.objects.get(pk=submission_id)
    body = (
        f"Name: {submission.name}\n"
        f"Email: {submission.email}\n"
        f"Phone: {submission.phone}\n\n"
        f"{submission.message}"
    )
    send_mail(
        subject=f"IPADEV contact form: {submission.subject}",
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=settings.CONTACT_RECIPIENT_EMAILS,
        fail_silently=False,
    )
