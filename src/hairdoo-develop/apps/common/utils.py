# DJANGO IMPORT
from django.apps import apps
from django.conf import settings

# REST IMPORT
from rest_framework.response import Response
from rest_framework import status as ResponseStatus

# LOCAL IMPORT
from .models import model_app


error_msg = 'Please fill missing field(s) or solve error(s)'


def get_model(model):
    model = model_app[model]
    model = model.split(".")
    return apps.get_model(model[0], model[1])


def get_compiled_model(model):

    model = model.split(".")
    return apps.get_model(model[0], model[1])


def get_object(model, query):

    model = get_compiled_model(model)

    try:
        return model.objects.get(**query)
    except model.DoesNotExist:
        return None


def filter_query(model, query):

    model = get_model(model)

    return model.objects.filter(**query)


def ReturnResponse(message=error_msg, data={}, status=False, code=ResponseStatus.HTTP_200_OK):

    return Response({
        'status': status,
        'code': code,
        'message': message,
        'data': data
    }, code)


def SerializeResponse(data, serializer, save=False, id=None, partial=False, many=False, context={}):

    message = ''

    if id:
        serializer = serializer(
            id, data=data, partial=partial, many=many, context=context)
        message = 'Data updated successfully'
    else:
        serializer = serializer(data=data, many=many, context=context)

    if serializer.is_valid():
        if save:
            message = 'Data save successfully'
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


def FetchSerializeResponse(data, serializer, many=False, context={}):

    if not data:
        if many:
            return ReturnResponse(
                status=False,
                data=[],
                message='Data not found'
            )
        else:
            return ReturnResponse(
                status=False,
                data={},
                message='Data not found'
            )

    serializer = serializer(data, many=many, context=context)

    return ReturnResponse(
        status=True,
        message="Data fetch successfully",
        data=serializer.data
    )


def build_absolute_uri(path):
    return settings.SITE_URL + path
