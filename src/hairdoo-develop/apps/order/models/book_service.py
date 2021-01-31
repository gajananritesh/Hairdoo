# DJANGO IMPORT
from django.db import models
from django.utils import timezone

# LOCAL IMPORT
from authentication.models import CommonModel
from common.models import model_app


class BookService(CommonModel):

    order = models.ForeignKey(model_app['order'], on_delete=models.CASCADE)
    service = models.ForeignKey(model_app['service'], on_delete=models.CASCADE)
    quantity = models.IntegerField()
