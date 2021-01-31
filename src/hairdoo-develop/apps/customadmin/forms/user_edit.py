# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from order.models import OrderDetail
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group, Permission
from authentication.models import Account
#from ..utils import filter_perms
from django.template import loader

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------

class MyRegistredUserChangeForm(UserChangeForm):
    """Custom UserChangeForm."""
    class Meta(UserChangeForm.Meta):
        model = OrderDetail
        fields = [
            'full_name',
            'full_address',
            'zip_code',
            'state',
            'note',
            'book_by',
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit)
        return instance

class MyRegistredUserNameForm(UserChangeForm):
    """Custom UserChangeForm."""
    class Meta(UserChangeForm.Meta):
        model = Account
        fields = [
            'first_name',
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit)
        return instance
