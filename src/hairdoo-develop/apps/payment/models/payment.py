from django.db import models
from authentication.models import CommonModel

from common.models import model_app


class Payment(CommonModel):

    order = models.ForeignKey(model_app['order'], on_delete=models.CASCADE)
    trasaction_id = models.CharField(max_length=200)
    card = models.ForeignKey(
        model_app['card_management'], on_delete=models.CASCADE)
    discount = models.FloatField()
    price = models.FloatField()
    tip = models.CharField(max_length=20, null=True, blank=True)
    tip_price = models.FloatField(default=0)
    is_done = models.BooleanField(default=False)
