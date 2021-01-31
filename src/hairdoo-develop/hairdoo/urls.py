"""hairdoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import path, include
from django.contrib import admin
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from order.views import ChangeOrderStatus
from django.conf.urls.static import static
from django.conf import settings


from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from customadmin.views import UserListView
api = 'api/'
version_1 = 'v1/'


urlpatterns = [
    path('admin/', admin.site.urls),
    path(api+version_1, include('authentication.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    path(api+version_1, include('social_account.urls')),
    path(api+version_1, include('order.urls')),
    path(api+version_1, include('payment.urls')),

    path("", TemplateView.as_view(template_name="core/index.html"), name="home"),
    
    # Django Admin, use {% url 'admin:index' %}
    #path(settings.ADMIN_URL, admin.site.urls),

    path("customadmin/", include("customadmin.urls")),
    
  
    path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path(
        'socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),

    path('order/<str:uuid>', ChangeOrderStatus.as_view(),
         name='Order-API'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
