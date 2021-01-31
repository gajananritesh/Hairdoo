# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from authentication.models import Account
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group, Permission

#from ..utils import filter_perms
from django.template import loader

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------

class MyUserChangeForm(UserChangeForm):
    """Custom UserChangeForm."""
    CHOICES = [
        ('straight','Straight'),
        ('curly','Curly'),
        ('long','Long'),
    ]

    address = forms.CharField(required=False,widget=forms.Textarea)
    hair_type = forms.CharField(widget=forms.Select(choices=CHOICES))
    class Meta(UserChangeForm.Meta):
        model = Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'hair_type',

        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit)
        return instance


            
        
    

