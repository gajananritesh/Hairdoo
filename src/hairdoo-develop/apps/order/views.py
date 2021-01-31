# DJANGO IMPORT
from django.views import View
from django.shortcuts import render, redirect

# REST IMPORT
from rest_framework.views import APIView

# LOCAL IMPORT
from .serializers import (MyDetailSerializer, ScheduleSerializer, DescriptionSerializer,
                          TrackerSerializer, BookServiceSerializer, OrderDetailsSerializer)

from common.utils import (SerializeResponse, get_object, get_model,
                          FetchSerializeResponse, filter_query)
from common.models import model_app
from common.permissions import isAuthenticated, isVerified

from payment.views import PaymentAPIView

from .models.order_detail import OrderDetail

import uuid

from django.db.models import Q


class MyDetailAPIView(APIView):

    """
        Mydetails API view to store user order
    """

    serializer = MyDetailSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request):

        return SerializeResponse(request.data, self.serializer, save=True)

    def put(self, request, id):

        id = get_object(model_app['order'], {'id': id})

        return SerializeResponse(request.data, self.serializer, save=True, id=id)


class ScheduleAPIView(APIView):

    """
        schedule user's order
    """

    serializer = ScheduleSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request, id):

        id = get_object(model_app['order'], {'id': id})

        return SerializeResponse(request.data, self.serializer, save=True, id=id)


class DescriptionAPIView(APIView):

    """
        user's order description
    """

    serializer = DescriptionSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request, id):

        id = get_object(model_app['order'], {'id': id})

        return SerializeResponse(request.data, self.serializer, save=True, id=id)


class TrackerAPIView(APIView):

    """
        user's order description
    """

    serializer = TrackerSerializer
    permission_classes = [isAuthenticated, isVerified]

    def get(self, request, id):

        id = get_object(model_app['order'], {'id': id})

        return FetchSerializeResponse(id, self.serializer)


class BookServiceAPIView(APIView):

    """
        Book service api view to store user order
    """

    serializer = BookServiceSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request, id):

        id = filter_query(
            'book_service', {'order__id': id, 'order__book_by': request.user})

        id.delete()

        return SerializeResponse(request.data, self.serializer, save=True, many=True)


class OrderDetailsAPIView(APIView):

    """
        Book service api view to store user order
    """

    serializer = OrderDetailsSerializer
    permission_classes = [isAuthenticated, isVerified]

    def get(self, request, id):

        id = get_object(model_app['order'], {'id': id})

        return FetchSerializeResponse(id, self.serializer)


class RebookOrderAPIView(APIView):

    serializer = OrderDetailsSerializer
    permission_classes = [isAuthenticated, isVerified]
    payment_api = PaymentAPIView

    def post(self, request, id):

        data = self.payment_api().post(request)

        order = get_object(model_app['order'], {'id': id})
        order.pk = None
        order.is_reorder = True
        order.unique_id = str(uuid.uuid4())
        order.status = 'CONFIRM'
        order.save()

        book_services = filter_query('book_service', {'order__id': id})

        for service in book_services:
            obj = service
            obj.order = order
            obj.pk = None
            obj.save()

        return FetchSerializeResponse(order, self.serializer)


class ChangeOrderStatusAPI(APIView):

    """
        Chagen order status
    """

    serializer = TrackerSerializer
    permission_classes = [isAuthenticated, isVerified]

    def post(self, request, id):

        order = get_object(model_app['order'], {
            'id': id, 'book_by': request.user})
        if order:
            status = request.data.get('status')
            order.status = status
            order.save()

        return FetchSerializeResponse(order, self.serializer)


class ChangeOrderStatus(View):

    template = 'base.html'

    def get(self, request, uuid):
        order = get_object(model_app['order'], {'unique_id': uuid})

        return render(request, self.template, context={"order": order})

    def post(self, request, uuid):
        order = get_object(model_app['order'], {'unique_id': uuid})
        status = request.POST.get('status')
        if status:
            order.status = status
            order.save()
        return redirect(f'/order/{uuid}')


class RecentBookingAPIView(APIView):

    serializer = OrderDetailsSerializer
    permission_classes = [isAuthenticated, isVerified]

    def get(self, request):

        # order = filter_query('order', {"status": "SENT"})
        # order = order.filter
        order = OrderDetail.objects.filter(Q(status='SENT') | Q(
            status="CONFIRM"), book_by=request.user).order_by("-id").first()

        return FetchSerializeResponse(order, self.serializer)
