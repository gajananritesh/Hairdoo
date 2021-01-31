# PYTHON IMPORT
from datetime import datetime

# DJANOG IMPORTS
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework import status as ResponseStatus

# REST IMPORTS
from rest_framework.views import APIView

# THIRD PARTY

# LOCAL IMPORTS
from common.utils import (
    ReturnResponse, SerializeResponse, FetchSerializeResponse,)

from .utils import check_otp_expire, generate_otp, send_otp

from .serializers import (RegistrationSerializer, LoginSerializer,
                          LoginDetailsSerializer, ForgotPasswordSerializer,
                          HairProfileSerializer, UserDetailsSerializer,
                          ServiceSerializer, ChangePassword, UnverifiedUserSerializer)
from common.utils import get_object, filter_query
from common.models import auth_app
from common.permissions import isAuthenticated, isVerified


class RegistrationAPIView(APIView):

    # User registraton API view

    serializer = RegistrationSerializer
    detailserializer = UserDetailsSerializer

    def post(self, request):

        serializer = self.serializer(data=request.data)

        # Check serializer is valid not
        if not serializer.is_valid():

            return ReturnResponse(data=serializer.errors)

        serializer.save()

        obj = get_object(auth_app['account'], {
                         'email': serializer.data.get('email')})

        serializer2 = self.detailserializer(obj)

        if serializer.data.get('account_type') == 'S':
            #send_otp(obj.otp, obj.phone)
            pass
        else:
            obj.verify = True
            obj.save()

        return ReturnResponse(message='Register successsfully', data=serializer2.data, status=True)


class LoginAPIView(APIView):

    serializer = LoginSerializer
    userserializer = LoginDetailsSerializer
    unverified_user = UnverifiedUserSerializer
    model = auth_app['account']

    # User login API view

    def post(self, request):

        serializer = self.serializer(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            account_type = serializer.data.get('account_type')
            social_id = serializer.data.get('social_id')

            if account_type == 'A' or account_type == 'F':

                user_exist = filter_query(
                    'account', query={'email': email, "account_type": account_type}).exists()

                if not user_exist:

                    return ReturnResponse(message='User is not register with this account',
                                          code=ResponseStatus.HTTP_202_ACCEPTED)

                obj = get_object(model=self.model, query={
                    'email': email, 'social_id': social_id})

                if obj:

                    return ReturnResponse(message='Login successfully',
                                          data=self.userserializer(obj).data,
                                          status=True)
                else:

                    return ReturnResponse(message='User is not register with this account')

            auth = authenticate(email=email, password=password)

            # ----check user is authenticated or not----
            if auth is not None:

                # ----check user in verified or not----
                if not auth.verify:
                    return ReturnResponse(message='This account is unverified',
                                          code=ResponseStatus.HTTP_201_CREATED,
                                          data=self.unverified_user(auth).data)

                login(request, auth)

                return ReturnResponse(message='Login successfully',
                                      data=self.userserializer(auth).data,
                                      status=True)

            else:
                return ReturnResponse(message='Invalid email or password',
                                      data=serializer.errors)

        return ReturnResponse(data=serializer.errors)


class VerifyAPIView(APIView):

    # OTP verification views

    model = auth_app['account']

    def post(self, request):

        code = request.data.get('code', '0')
        email = request.data.get('email', '')
        obj = get_object(model=self.model, query={'email': email, 'otp': code})

        # ----OTP match----
        if obj:

            # ----Check already verified----
            if obj.verify:
                return ReturnResponse(message='This account is already verified',
                                      status=False)

            # ----OTP expiration----
            if check_otp_expire(obj.send_time):
                return ReturnResponse(message='OTP is expired',
                                      status=False)
            obj.verify = True
            obj.save()
            return ReturnResponse(message='Account verified successfully',
                                  status=True)
        return ReturnResponse(message='Invalid OTP',
                              status=False)


class ForgotPasswordAPIView(APIView):

    # Forgot password view

    model = auth_app['account']

    def post(self, request):

        email = request.data.get('email', '')
        obj = get_object(model=self.model, query={'email': email})

        # Account exist
        if obj:
            obj.forgot_otp = generate_otp()
            obj.forgot_time = datetime.now()
            send_otp(obj.forgot_otp, obj.phone)
            obj.save()
            return ReturnResponse(message='OTP send on mobile to change password',
                                  status=True)
        return ReturnResponse(message='Account with this email is not register',
                              status=False)


class VerifyForgotPasswordAPIView(APIView):

    # Check forgot password OTP verification views

    model = auth_app['account']
    serializer = ForgotPasswordSerializer

    def post(self, request):

        serializer = self.serializer(data=request.data)

        if not serializer.is_valid():

            return ReturnResponse(data=serializer.errors,
                                  status=False)

        code = request.data.get('code', '0')
        email = request.data.get('email', '')

        obj = get_object(model=self.model, query={
                         'email': email, 'forgot_otp': code})

        # OTP match
        if obj:

            # OTP expiration-
            if check_otp_expire(obj.forgot_time):
                return ReturnResponse(message='OTP is expired',
                                      status=False)
            # Set password
            obj.set_password(serializer.data.get('password'))
            obj.save()

            return ReturnResponse(message='Password changed successfully',
                                  status=True)

        return ReturnResponse(message='Invalid OTP',
                              status=False)


class AddHairProfileAPIView(APIView):

    # Add hair profile view

    model = auth_app['hair_profile']
    serializer = HairProfileSerializer

    def post(self, request):

        return SerializeResponse(request.data, self.serializer, save=True)


class EditHairProfileAPIView(APIView):

    # Edit hair profile view

    serializer = HairProfileSerializer

    def post(self, request, id):
        id = get_object(auth_app['hair_profile'], {'id': id})
        return SerializeResponse(request.data, self.serializer, save=True, id=id, partial=True)


class ServiceAPIView(APIView):

    # All service api view

    serializer = ServiceSerializer

    def get(self, request):

        query = filter_query('service', {'active': True})

        return FetchSerializeResponse(query, self.serializer, many=True)


class ChangePasswordAPIView(APIView):

    # All service api view

    permission_classes = [isAuthenticated, isVerified]
    serializer = ChangePassword

    def post(self, request):

        return SerializeResponse(request.data, self.serializer, save=True, context={"user": request.user})


class ResendOTPAPIView(APIView):

    # Resend OTP

    model = auth_app['account']

    def post(self, request):

        email = request.data.get('email')
        obj = get_object(model=self.model, query={'email': email})

        # Account exist
        if obj:
            obj.otp = generate_otp()
            obj.send_time = datetime.now()
            send_otp(obj.otp, obj.phone)
            obj.save()
            return ReturnResponse(message='OTP send on mobile to change password',
                                  status=True)
        return ReturnResponse(message='Account with this email is not register',
                              status=False)
