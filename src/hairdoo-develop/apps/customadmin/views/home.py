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
from django.shortcuts import redirect,render
from ..forms import MyUserChangeForm
from order.models import OrderDetail
from authentication.models import Account
from django.contrib import messages
from http import HTTPStatus
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"


class UserListView(MyListView):
    """View for User listing"""

    model = OrderDetail
    template_name = "core/index.html"
    permission_required = ("core.view_user",)

    def get_queryset(self):       
        return self.model.objects.filter(status = "PROGRESS").order_by("-created_at")[:6]

class AllUserListView(MyListView):
    """View for all User listing"""

    model = OrderDetail
    template_name = "core/index.html"
    permission_required = ("core.view_user",)

    def get_queryset(self):       
        return self.model.objects.filter(status = "PROGRESS").order_by("-created_at")

class UserUpdateView(MyUserUpdateView):

    """View to update User"""

    model = Account
    form_class = MyUserChangeForm
    template_name = "core/profile.html"
    permission_required = ("core.change_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

class UserPasswordView(MyPasswordUpdateView):
    """View to change User Password"""

    model = Account
    form_class = AdminPasswordChangeForm
    template_name = "core/change-password.html"
    permission_required = ("core.change_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs['user'] = self.request.user
        kwargs["user"] = kwargs.pop("instance")
        return kwargs

class RegisteredUserListView(MyListView):
    """View for User listing"""

    model = OrderDetail
    template_name = "core/user.html"
    permission_required = ("core.view_user",)

    def get_queryset(self):       
        return self.model.objects.all().distinct('book_by')

def ProjectDeleteView(request):
    get_id = request.POST['get_id']
    print(get_id)
    if get_id:
        #Account.objects.get(id=get_id).delete()
        response = {
        'status': 'updated',
        'ok': True
        }
        print("???????????????????????")
        messages.success(request, "User deleted successfully")
        print("_______________________________________",response)
        #return JsonResponse(response)
        return redirect("/customadmin/registred-users")

    else:
        print("++++++++++++++++++++++++")
        response = {
        'status': 'Error',
        'ok': False,
        'errors':"error"
        }
        messages.success(request, "Error while deleting user!")
        print("____________________++++++++++++___________________",response)

        return JsonResponse(response)
