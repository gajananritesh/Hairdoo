# DJANGO IMPORTS
from django.conf import settings

# REST_FRAMEWORK
from rest_framework import serializers

# LOCAL IMPORT
from common.utils import get_model, build_absolute_uri, filter_query
from payment.serializers import CardSerializer

# THIRD PARTY
import stripe


OrderDetail = get_model('order')
Artist = get_model('artist')
BookService = get_model('book_service')
Service = get_model('service')


stripe.api_key = settings.STRIPE_KEY


class MyDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderDetail
        fields = ['id', 'book_by', 'full_address',
                  'apt_no', 'zip_code', 'state', 'note']


class ScheduleSerializer(serializers.ModelSerializer):

    earliest = serializers.DateTimeField(required=True, allow_null=False,
                                         format="%Y-%m-%d %H:%M:%S")
    latest = serializers.DateTimeField(required=True, allow_null=False,
                                       format="%Y-%m-%d %H:%M:%S")

    class Meta:

        model = OrderDetail
        fields = ['id', 'earliest', 'latest']


class DescriptionSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=True, allow_null=True)

    class Meta:

        model = OrderDetail
        fields = ['id', 'description']


class TrackerSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderDetail
        fields = ['id', 'status', 'created_at']


class BookServiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = BookService
        fields = ['id', 'order', 'service', 'quantity']


class ArtistSerializer(serializers.ModelSerializer):

    profile_image = serializers.SerializerMethodField('get_profile_image')

    class Meta:

        model = Artist
        fields = ['id', 'name', 'profile_image']

    def get_profile_image(self, obj):

        if obj.profile_image:

            return build_absolute_uri(obj.profile_image.url)

        return ''


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Service
        fields = ['id', 'name', 'price']


class BookServiceDetailsSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:

        model = BookService
        fields = ['id', 'order', 'service', 'quantity']


class OrderDetailsSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer()
    book_services = serializers.SerializerMethodField('get_book_services')
    card = serializers.SerializerMethodField('get_card')

    class Meta:

        model = OrderDetail
        fields = ['id', 'book_by', 'artist', 'full_address',
                  'apt_no', 'zip_code', 'state', 'note', 'earliest',
                  'latest', 'description', 'status', 'book_services', 'card']

    def get_book_services(self, obj):

        query = filter_query('book_service', {'order__pk': obj.pk})
        return BookServiceDetailsSerializer(query, many=True).data

    def get_card(self, obj):

        query = filter_query('card_management', {'user__id': obj.book_by.id})
        data = query.last()
        data = query.first()

        if data:
            try:
                customer = stripe.Customer.retrieve(
                    data.stripe_customer_id)
                return {"card_id": data.id, "last4": f"**** **** **** {customer.sources.data[0].last4}"}
            except Exception:
                return None

        return None
