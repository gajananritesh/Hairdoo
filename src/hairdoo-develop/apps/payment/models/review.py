from django.db import models
from authentication.models import CommonModel

from common.models import model_app

class Review(CommonModel):
    
    class STATUS(models.TextChoices):

        YES = 'YES'
        NO = 'NO'
        NOT_SURE = 'NOT_SURE'
    
    user = models.ForeignKey(model_app['account'], on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(model_app['artist'], on_delete=models.CASCADE, null=True)
    book_again = models.CharField(max_length=10, choices=STATUS.choices)
    star = models.FloatField()
    technique = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    professionalism = models.BooleanField(default=False)
    timeliness = models.BooleanField(default=False)
    persionality = models.BooleanField(default=False)
    note = models.TextField()