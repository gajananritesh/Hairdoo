from django.db import models
from authentication.models import CommonModel

from common.models import model_app


class CardManagement(CommonModel):

    number = models.CharField(max_length=500)
    stripe_token = models.CharField(max_length=500,
                                    null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=500,
                                          null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    cvv = models.CharField(max_length=10, null=True, blank=True)
    default = models.BooleanField(default=False)
    user = models.ForeignKey(model_app['account'],
                             on_delete=models.CASCADE)
    expiry = models.DateField(null=True, blank=True)
