# DJANGO IMPORTS
from django.conf import settings


# REST IMPORT
from rest_framework import serializers

# LOCAL IMPORT
from common.utils import get_model, filter_query
from common.models import model_app
from .utils import send_email_artist

# THIRD PARTY
import stripe


CardManagement = get_model('card_management')
Review = get_model('review')
Payment = get_model('payment')


stripe.api_key = settings.STRIPE_KEY


class CardSerializer(serializers.ModelSerializer):

    stripe_token = serializers.CharField(
        required=True, allow_blank=False, allow_null=False)
    number = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    country = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    cvv = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    default = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    expiry = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = CardManagement
        fields = ['id', 'number', 'stripe_token', 'stripe_customer_id',
                  'country', 'cvv', 'default', 'user', 'expiry']

    def validate(self, data):

        try:

            customer = stripe.Customer.create(
                description="New Card Payment",
                source=data['stripe_token'],
                name=data['user'].first_name+data['user'].last_name,
                email=data['user'].email
            )

            data['stripe_customer_id'] = customer.id

        except Exception as e:

            raise serializers.ValidationError(e)

        return data


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'user', 'artist', 'book_again', 'star', 'technique', 'service',
                  'professionalism', 'timeliness', 'persionality', 'note']

    def validate(self, data):

        if data['star'] > 5:

            raise serializers.ValidationError('Star should be less then 5')

        return data


class PaymentSerializer(serializers.ModelSerializer):

    is_done = serializers.SerializerMethodField('get_is_done')
    trasaction_id = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Payment
        fields = ['id', 'order', 'trasaction_id', 'card',
                  'discount', 'price', 'is_done']

    def validate(self, data):

        try:
            charge = stripe.Charge.create(
                customer=data['card'].stripe_customer_id,
                amount=int(data['price']*100),
                currency="usd",
                description="Payment By Card",
            )
            data['trasaction_id'] = charge.id
        except Exception as e:

            raise serializers.ValidationError(e)

        return data

    def get_is_done(self, obj):
        artist = filter_query('artist', {'active': True})
        obj.order.artist = artist.order_by('?').first()
        obj.order.is_complete = True
        obj.order.status = 'CONFIRM'
        obj.order.save()
        obj.is_done = True
        obj.save()

        send_email_artist(obj.order)
        return True


class TipSerializer(serializers.ModelSerializer):

    tip = serializers.CharField(required=True, allow_blank=False,
                                allow_null=False)
    tip_price = serializers.FloatField(required=True)

    card = serializers.PrimaryKeyRelatedField(
        queryset=filter_query('card_management', {}))

    class Meta:
        model = Payment
        fields = ['id', 'tip', 'tip_price', 'card']

    def validate(self, data):

        charge = stripe.Charge.create(
            customer=data['card'].stripe_customer_id,
            amount=int(data['tip_price']*100),
            currency="usd",
            description="Payment By Card for tips",
        )

        return data
