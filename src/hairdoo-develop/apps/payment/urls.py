from django.urls import path

# LOCAL IMPORT
from .views import (AddCardAPIView, AllCardsAPIView, AddReviewAPIView,
                    PaymentAPIView, StripeTokenApi, TipAPIView, DefaultCardAPIView)

urlpatterns = [
    path('add-card/', AddCardAPIView.as_view(), name='Add-card-API'),
    path('add-card/<int:id>', AddCardAPIView.as_view(), name='Add-card-API'),
    path('all-card/', AllCardsAPIView.as_view(), name='all-card-API'),
    path('add-review/', AddReviewAPIView.as_view(), name='Add-review-API'),
    path('payment/', PaymentAPIView.as_view(), name='Payment-API'),
    path('stripe-token/', StripeTokenApi.as_view(), name='StripeToken-API'),
    path('tip/<int:id>', TipAPIView.as_view(), name='StripeToken-API'),
    path('make-default-card/<int:id>',
         DefaultCardAPIView.as_view(), name='Make-Default-Card-API'),
    path('get-default-card/',
         DefaultCardAPIView.as_view(), name='Get-Default-Card-API'),
]
