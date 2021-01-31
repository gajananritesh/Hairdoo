from django.core.mail import EmailMultiAlternatives
from rest_framework.pagination import PageNumberPagination
from smtplib import SMTPException
from django.conf import settings


def send_email(**data):
    msg = EmailMultiAlternatives(
        data["subject"],
        data["text_content"],
        settings.EMAIL_HOST_USER, [data['email']],
        [settings.EMAIL_HOST_BCC]
    )
    try:
        msg.attach_alternative(data["text_content"], "text/html")
        msg.send()
    except SMTPException:
        return False
    return True


def send_email_user(order):

    user = order.book_by
    artist = order.artist

    subject = 'HairDoo Service Booking'
    text_content = f'Hello {user.first_name} {user.last_name}<br><br>'
    text_content += f'You have book service successfully<br><br>'
    text_content += f'and your artist name is {artist.name}<br><br>'
    text_content += 'Thank you'

    send_email(subject=subject, text_content=text_content, email=user.email)


def send_email_artist(order):

    artist = order.artist

    subject = 'HairDoo Service Booking'
    text_content = f'Hello {artist.name}<br>'
    text_content += f'Please click on below link<br>and check that new service has been booked<br><br>'
    text_content += f'{settings.SITE_URL}/order/{order.unique_id}<br><br>'
    text_content += 'Thank you'

    send_email_user(order)
    send_email(subject=subject, text_content=text_content, email=artist.email)
