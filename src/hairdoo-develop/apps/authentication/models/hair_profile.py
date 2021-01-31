from django.db import models
from .common_model import CommonModel
from common.models import auth_app


class HairProfile(CommonModel):

    class STYLE_CHOICES(models.TextChoices):

        NA = 'NA'
        STRAIGHT = 'STRAIGHT'
        WAVY = 'WAVY'
        CURLY = 'CURLY'

    class TEXTURE_CHOICES(models.TextChoices):

        NA = 'NA'
        FINE = 'FINE'
        MEDIUM = 'MEDIUM'
        COARSE = 'COARSE'

    class LENGTH_CHOICES(models.TextChoices):

        NA = 'NA'
        BALD = 'BALD'
        SHORT = 'SHORT'
        LONG = 'LONG'

    user = models.OneToOneField(auth_app['account'], on_delete=models.CASCADE)
    style = models.CharField(choices=STYLE_CHOICES.choices, max_length=10)
    texture = models.CharField(choices=TEXTURE_CHOICES.choices, max_length=10)
    length = models.CharField(choices=LENGTH_CHOICES.choices, max_length=10)
