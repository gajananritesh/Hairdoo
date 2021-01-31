from django.shortcuts import redirect, render,HttpResponse
from authentication.models import Account,Service
from order.models import BookService, OrderDetail
from ..views import UserBookingListView
def edit_booking(request,id):
    if request.method == 'POST':
        # First form data
        hr_standerd = request.POST['hr_standerd']
        address = request.POST['address']
        zip = request.POST['zip']
        state = request.POST['state']
        schedule_date = request.POST['schedule_date']
        # second form data 
        quantity_men = request.POST['q_men']
        price_men = request.POST['p_men']
        quantity_women = request.POST['q_women']
        price_women = request.POST['p_women']
        quantity_beard = request.POST['q_beard']
        price_beard = request.POST['p_beard']
        quantity_blow = request.POST['q_blow']
        price_blow = request.POST['p_blow']
        print(request.POST)
        obj = OrderDetail.objects.get(id = id)
        #user_obj = booked_service_obj.order
        obj.full_address = address
        obj.zip_code = zip
        obj.state = state
        obj.earliest = schedule_date
        obj.save()
        context = {
             'db_address':obj.full_address ,'db_zip': obj.zip_code ,'db_state' : obj.state,'db_schedule_date': obj.earliest
        }
        men_hair_obj = Service.objects.get(id=1)
        women_hair_obj = Service.objects.get(id=3)
        beard_obj = Service.objects.get(id=2)
        blow_obj = Service.objects.get(id=4)
        if len(quantity_men)>0 and int(quantity_men)!=0:
            BookService(order = obj,service=men_hair_obj,quantity=quantity_men).save()
        if len(quantity_women)>0 and int(quantity_women)!=0:
            BookService(order = obj,service=women_hair_obj,quantity=quantity_women).save()
        if len(quantity_beard)>0 and int(quantity_beard)!=0:
            BookService(order = obj,service=beard_obj,quantity=quantity_beard).save()
        if len(quantity_blow)>0 and int(quantity_blow)!=0:
            BookService(order = obj,service=blow_obj,quantity=quantity_blow).save()
        print(obj.earliest)
        return redirect('/customadmin/bookings/')
        
    else:
        obj = OrderDetail.objects.get(id = id)
        context = {
           'db_address' :obj.full_address , 'db_zip': obj.zip_code ,'db_state' : obj.state
        }
        return render(request,"core/edit-booking.html",context=context)