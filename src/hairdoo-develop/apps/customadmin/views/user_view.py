from .generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUserUpdateView,
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
#from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory



class UserDetailView(MyListView):

    """View to update User"""

    model = OrderDetail
    template_name = "core/view-user.html"
    permission_required = ("core.change_user",)

    def get_queryset(self):       
        return self.model.objects.get(pk = self.kwargs['pk'])
