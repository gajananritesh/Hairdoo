from django.db import models
from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.


class AccountManager(BaseUserManager):

    def create_user(self, **kwargs):

        account = self.model(
            email=self.normalize_email(kwargs.get('email')),
            username=kwargs.get('email')
        )

        account.set_password(kwargs.get('password'))
        account.send_time = datetime.now()
        account.save()

        return account

    def create_superuser(self, **kwargs):

        account = self.create_user(**kwargs)
        account.is_staff = True
        account.is_superuser = True
        account.is_active = True
        account.otp = 000000
        account.save()

        return account


class Account(AbstractBaseUser, PermissionsMixin):
    CHOICES = [
        ('straight','Straight'),
        ('curly','Curly'),
        ('long','Long'),

    ]

    class AccountType(models.TextChoices):

        F = 'F'
        A = 'A'
        S = 'S'

    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=500)

    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    phone = models.CharField(max_length=17,
                             blank=True, null=True)
    otp = models.IntegerField(default=000000)
    send_time = models.DateTimeField()
    verify = models.BooleanField(default=False)

    forgot_otp = models.IntegerField(default=000000)
    forgot_time = models.DateTimeField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    account_type = models.CharField(max_length=5, choices=AccountType.choices,
                                    default=AccountType.S)

    social_id = models.CharField(max_length=500, null=True, blank=True)

    objects = AccountManager()
    address = models.TextField(max_length=500, null=True, blank=True)
    hair_type = models.CharField(choices=CHOICES, max_length=10,null=True,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)    
