from django.db import models
from authentication.models import CommonModel


class Artist(CommonModel):

    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='artist_profile')
    email = models.CharField(max_length=300)
