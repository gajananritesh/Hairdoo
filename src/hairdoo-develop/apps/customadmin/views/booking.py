from .generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUserUpdateView,
    MyView,
    MyPasswordUpdateView
)
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.utils.text import Truncator
from django.views.generic import TemplateView
#from django_datatables_too.mixins import DataTableMixin
from django.contrib import messages
from http import HTTPStatus
from ..forms import MyUserChangeForm, MyBookedUserChangeForm,MyAddServiceForm
from order.models import OrderDetail,BookService
from authentication.models import Account




class UserBookingListView(MyListView):
    """View for all User listing"""

    model = OrderDetail
    template_name = "core/booking.html"
    permission_required = ("core.view_user",)

    def get_queryset(self):       
        return self.model.objects.all().exclude(status='CONFIRM').exclude(status='SENT').order_by("-id")

class BookedServiceUserDetailView(MyListView):
    """View for all User listing"""

    model = BookService
    template_name = "core/view-booking.html"
    permission_required = ("core.view_user",)

    def get_queryset(self):       
        return self.model.objects.filter(order = self.kwargs['id'])

class EditServiceView(MyListView):
    """View for all User listing"""

    model = BookService
    template_name = "core/edit-booking.html"
    permission_required = ("core.view_user",)

    def get_queryset(self):       
        return self.model.objects.filter(order = self.kwargs['id'])        

#class BookingUpdateView(MyUserUpdateView):
#
#    """View to update User"""
#
#    model = BookService
#    form_class = MyUserChangeForm
#    template_name = "core/edit-booking.html"
#    permission_required = ("core.change_user",)
#
#    def get_form_kwargs(self):
#        kwargs = super().get_form_kwargs()
#        kwargs["order"] = self.kwargs['id']
#        return kwargs

def OrderDeleteView(request):
    get_id = request.POST['get_id']
    print(get_id)
    if get_id:
        obj = OrderDetail.objects.get(id=get_id)
        obj.delete()
        response = {
        'status': 'updated',
        'ok': True
        }
        print("???????????????????????")
        messages.success(request, "Deleted project successfully")
        return JsonResponse(response)

    else:
        print("++++++++++++++++++++++++")
        response = {
        'status': 'Error while updating',
        'ok': False,
        'errors':"error"
        }
        return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)

        