from authentication.models import Account
from order.models import OrderDetail

def get_user_count(request):
   return { 'total_user' : OrderDetail.objects.all().distinct('book_by').count() }

def get_order_number(request):
    return  { 'total_order' : OrderDetail.objects.filter(status='PROGRESS').count() }