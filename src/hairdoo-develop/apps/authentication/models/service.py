# DJANOG
from django.db import models

# LOCAL IMPORT
from authentication.models import CommonModel


class Service(CommonModel):

    name = models.CharField(max_length=400)
    price = models.FloatField()
