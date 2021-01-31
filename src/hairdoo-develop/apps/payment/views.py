# DJANGO IMPORT
from django.conf import settings

# THIRT PARTY
import stripe

# REST IMPORT
from rest_framework.views import APIView
from rest_framework.response import Response

# LOCAL IMPORT
from .serializers import (CardSerializer, ReviewSerializer,
                          PaymentSerializer, TipSerializer)
from common.utils import (
    SerializeResponse, FetchSerializeResponse, filter_query, get_object, model_app)

from common.permissions import isAuthenticated, isVerified

# Create your views here.

stripe.api_key = settings.STRIPE_KEY


class AddCardAPIView(APIView):

    """
        POST, PUT, GET card details API's
    """

    serializer = CardSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request):
        filter_query('card_management', {'user': request.user}).delete()
        return SerializeResponse(request.data, self.serializer, save=True)

    def get(self, request, id):

        data = get_object(model_app['card_management'], {'id': id})
        return FetchSerializeResponse(data, self.serializer)

    def put(self, request, id):

        id = get_object(model_app['card_management'], {'id': id})
        return SerializeResponse(request.data, self.serializer, save=True, id=id)


class AllCardsAPIView(APIView):

    """
        Get all details of cards API
    """

    serializer = CardSerializer
    permission_classes = [isAuthenticated, isVerified]

    def get(self, request):

        data = filter_query('card_management', {'user__id': request.user.id})
        return FetchSerializeResponse(data, self.serializer, many=True)


class AddReviewAPIView(APIView):

    """
        Add review API
    """

    serializer = ReviewSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request):

        return SerializeResponse(request.data, self.serializer, save=True)


class PaymentAPIView(APIView):

    """
        Add Payment deatils APIView
    """

    serializer = PaymentSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request):

        return SerializeResponse(request.data, self.serializer, save=True)


class StripeTokenApi(APIView):

    """
        Fetch stripe token APIView
    """

    def get(self, request, format=None):

        tokens = stripe.Token.create(
            card={"name": 'Atlas', "number": '4242424242424242',
                  "exp_month": '05', "exp_year": '2022', "cvc": '123'})

        return Response({
            "data": tokens.id,
            "status": True,
            "code": 200,
            "message": "Successfully fetched token"
        })


class TipAPIView(APIView):

    """
        Add Tips APIView
    """

    serializer = TipSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request, id):
        try:
            order = filter_query('order', {'id': id}).first()
            payment = filter_query('payment', {
                'order__id': order.id}).first()
            return SerializeResponse(request.data, self.serializer, save=True, id=payment)
        except AttributeError as e:
            print("-------------", e)
            return Response({
                "status": False,
                "code": 200,
                "message": "Please make you sure pass right order id",
                "data": {}
            })


class DefaultCardAPIView(APIView):

    """
        Add Payment deatils APIView
    """

    serializer = CardSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request, id):

        data = filter_query('card_management',
                            {'user__id': request.user.id}
                            ).update(default=False)

        id = get_object(model_app['payment'], {
                        'id': id, 'user__id': request.user.id})
        id.default = True
        id.save()

        return SerializeResponse(request.data, self.serializer, save=True, id=id, partial=True)

    def get(self, request):

        data = get_object(model_app['card_management'],
                          {'user__id': request.user.id, 'default': True},
                          )

        return FetchSerializeResponse(data, self.serializer)
