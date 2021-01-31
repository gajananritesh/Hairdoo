# PYTHON IMPORT
import random
from datetime import datetime, timedelta


# DJANGO IMPORT
from django.conf import settings

# REST_FRAMEWORK IMPORT
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status as ResponseStatus
from rest_framework.response import Response

# THIRD PARTY
from twilio.rest import Client

# LOCAL IMPORT
from common.utils import get_object, get_model
from common.models import auth_app


error_msg = 'Please fill missing field(s) or solve error(s)'


def generate_otp():
    # return   str(random.randint(1111, 9999))
    return str(1234)


def get_or_create_token(user):

    return Token.objects.get_or_create(user=user)


def ReturnResponse(message=error_msg, data={}, status=False):

    return Response({
        'status': status,
        'code': ResponseStatus.HTTP_200_OK,
        'message': message,
        'data': data
    }, ResponseStatus.HTTP_200_OK)


def SerializeResponse(data, serializer, save=False, id=None, partial=False):

    message = ''

    if id:
        serializer = serializer(id, data=data, partial=True)
        message = 'Data updated successfully'
    else:
        serializer = serializer(data=data)
        message = 'Data save successfully'

    if serializer.is_valid():
        if save:
            serializer.save()
        return ReturnResponse(
            status=True,
            message=message,
            data=serializer.data
        )
    return ReturnResponse(
        status=False,
        data=serializer.errors
    )


def check_otp_expire(send_time):

    send_time = send_time + timedelta(seconds=120)

    if datetime.now() > send_time:

        return True
    return False


def send_otp(otp, number):
    try:
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        message = client.messages .create(
            body=f"{otp} is your HairDoo varification code",
            from_=settings.NUMBER,
            to=number
        )
    except Exception:
        # dataa
        pass
