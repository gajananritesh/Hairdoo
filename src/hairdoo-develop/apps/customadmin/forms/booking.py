# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from order.models import OrderDetail, BookService
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group, Permission
from authentication.models import Account
#from ..utils import filter_perms
from django.template import loader

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------

class MyBookedUserChangeForm(forms.Form):
    """Booked UserChangeForm."""
    class Meta():
        model = OrderDetail
        fields = [
            'full_address',
            'zip_code',
            'state',
            'earliest',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit)
        return instance

class MyAddServiceForm(forms.Form):
    """Add Service UserChangeForm."""
    class Meta():
        model = BookService
        fields = [
            '',
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit)
        return instance
