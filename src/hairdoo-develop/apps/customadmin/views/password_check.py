from django.shortcuts import render,HttpResponse
# Create your views here.
from authentication.models import Account
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def is_corrrect_password(request):
    if request.method == 'POST':
        print("((((((((((((((((((((((")
        password = request.POST['password']
        admin_obj = Account.objects.filter(is_superuser = True).first()
        print(admin_obj.password)
        print(admin_obj.check_password(password))
        if admin_obj.check_password(password):
            return HttpResponse('correct')
        else:
            return HttpResponse('wrong')



