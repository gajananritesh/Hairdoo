# DJANGO IMPORT
from django.db import models
from django.utils import timezone
import uuid

# LOCAL IMPORT
from authentication.models import CommonModel
from common.models import model_app


class OrderDetail(CommonModel):

    class STATUS_CHOICES(models.TextChoices):

        SENT = 'SENT'
        CONFIRM = 'CONFIRM'
        ON_WAY = 'ON_WAY'
        ARRIVING = 'ARRIVING'
        PROGRESS = 'PROGRESS'
        COMPLETE = 'COMPLETE'

    book_by = models.ForeignKey(model_app['account'], on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,blank=True,null=True)
    full_address = models.TextField()
    apt_no = models.CharField(max_length=100)
    artist = models.ForeignKey(
        model_app['artist'], on_delete=models.CASCADE, null=True, blank=True)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=500)
    note = models.TextField(null=True, blank=True)
    earliest = models.DateTimeField(null=True, blank=True)
    latest = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    status = models.CharField(
        choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.SENT, max_length=15)
    is_reorder = models.BooleanField(default=False)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)

    

