from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        subject='Welcome!',
        message='Thanks for signing up!',
        from_email='arjun07ranawat@gmail.com', 
        recipient_list=[user_email],
        fail_silently=False,
    )
