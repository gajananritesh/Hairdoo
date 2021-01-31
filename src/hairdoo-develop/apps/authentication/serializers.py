# PYTHON IMPORT
from datetime import datetime

# DJANGO IMPORT

# REST IMPORT
from rest_framework.serializers import ModelSerializer, BaseSerializer
from rest_framework import serializers

# THIRD PARTY

# LOCAL IMPORT
from .utils import generate_otp, get_or_create_token
from common.models import auth_app
from common.utils import get_model, get_object


Account = get_model('account')
HairProfile = get_model('hair_profile')
Service = get_model('service')


class RegistrationSerializer(ModelSerializer):

    password = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)

    social_id = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)

    class Meta:

        model = Account
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'phone', 'account_type', 'social_id']

    def validate(self, data):

        if data.get('account_type') == 'S':

            if data.get('password') == "" or data.get('password') == None:
                raise serializers.ValidationError(
                    "password field cannot be blank or null")

            if Account.objects.filter(phone=data.get('phone', None)).exists():

                raise serializers.ValidationError(
                    "account with this phone already exists.")

        if data.get('account_type') == 'F' and data.get('account_type') == 'A':

            if data.get('social_id') == "" or data.get('social_id') == None:

                raise serializers.ValidationError(
                    "social_id field cannot be blank or null.")

        return data

    def save(self):

        data = self.data

        account = Account()
        account.first_name = data.get('first_name')
        account.last_name = data.get('last_name')
        account.email = data.get('email')
        account.username = data.get('email')
        account.set_password(data.get('password'))
        account.phone = data.get('phone')
        account.otp = generate_otp()
        account.send_time = datetime.now()
        account.account_type = data.get('account_type')
        account.social_id = data.get('social_id')
        account.save()

        get_or_create_token(account)

        return account


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    account_type = serializers.CharField(
        required=True, allow_null=False, allow_blank=False)
    social_id = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)

    class Meta:
        fields = [
            'email', 'password', 'account_type', 'social_id'
        ]

    def validate(self, data):

        account_type = ['F', 'A', 'S']

        account_type_data = data.get("account_type")

        if account_type_data not in account_type:
            raise serializers.ValidationError("invalid account_type")

        return data


class LoginDetailsSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = [
            'id', 'email', 'first_name', 'last_name', 'token',
        ]

    def get_token(self, data):
        return f'Token {get_or_create_token(data)[0]}'


class UnverifiedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'id', 'email', 'phone',
        ]


class UserDetailsSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = [
            'id', 'email', 'first_name', 'last_name',  'token',
        ]

    def get_token(self, data):
        return f'Token {get_or_create_token(data)[0]}'


class ForgotPasswordSerializer(serializers.ModelSerializer):

    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Account
        fields = [
            'code', 'password'
        ]


class ChangePassword(serializers.ModelSerializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = Account
        fields = [
            'old_password', 'new_password'
        ]

    def validate(self, data):
        user = self.context.get('user')
        check = user.check_password(data.get('old_password'))

        if not check:
            raise serializers.ValidationError('Old password not match')

        return data

    def save(self):
        user = self.context.get('user')
        user.set_password(self.data.get('new_password'))
        user.save()
        return self.data


class HairProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = HairProfile
        fields = [
            'id', 'user', 'style', 'texture', 'length',
        ]


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'price'
        ]
