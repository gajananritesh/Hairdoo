from .generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyRegistredUserUpdateView,
    MyView,
    MyPasswordUpdateView,
    MyNewFormsetUpdateView,

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

from ..forms import (MyRegistredUserChangeForm,)
from order.models import OrderDetail
from authentication.models import Account
#from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory#

##class RegisterUserInline(InlineFormSetFactory):
##    """Inline view to show PlanFeature within the Parent View"""
##
##    model = Account
##    form_class = MyRegistredUserNameForm
##
##    def get_form_kwargs(self):
##        kwargs = super().get_form_kwargs()
##        kwargs["user"] = self.request.user
#        return kwargs
#

class RegistredUserUpdateView(MyRegistredUserUpdateView):
    """View to update User"""
    model = OrderDetail
    #inline_model = Account
    #inlines = [RegisterUserInline, ]

    form_class = MyRegistredUserChangeForm
    template_name = "core/edit-user.html"
    permission_required = ("core.change_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

 