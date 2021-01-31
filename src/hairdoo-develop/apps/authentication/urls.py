from .views import (RegistrationAPIView, LoginAPIView, VerifyAPIView,
                    ForgotPasswordAPIView, VerifyForgotPasswordAPIView,
                    AddHairProfileAPIView, EditHairProfileAPIView,
                    ServiceAPIView, ChangePasswordAPIView, ResendOTPAPIView)
from django.urls import path


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='Register-API'),

    path('login/', LoginAPIView.as_view(), name='Login-API'),

    path('verify/', VerifyAPIView.as_view(), name='Verify-API'),

    path('forgot-password/',
         ForgotPasswordAPIView.as_view(), name='Forgot-Password-API'),

    path('verify-forgot-password/',
         VerifyForgotPasswordAPIView.as_view(), name='Verify-Forgot-Password-API'),

    path('add-hair-profile/',
         AddHairProfileAPIView.as_view(), name='Add-Hair-profile-API'),

    path('edit-hair-profile/<int:id>',
         EditHairProfileAPIView.as_view(), name='Edit-Hair-profile-API'),

    path('service/',
         ServiceAPIView.as_view(), name='Service-API'),


    path('change-password/',
         ChangePasswordAPIView.as_view(), name='Change-password-API'),

    path('resend-OTP/',
         ResendOTPAPIView.as_view(), name='Resend-OTP-API'),

]
