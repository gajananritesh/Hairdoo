from django.urls import path
from .views import (MyDetailAPIView, ScheduleAPIView, DescriptionAPIView,
                    TrackerAPIView, BookServiceAPIView, OrderDetailsAPIView,
                    RebookOrderAPIView, ChangeOrderStatus, ChangeOrderStatusAPI,
                    RecentBookingAPIView)


urlpatterns = [
    path('my-details', MyDetailAPIView.as_view(), name='MyDetails-API'),

    path('my-details/<int:id>', MyDetailAPIView.as_view(),
         name='MyDetails-Edit-API'),

    path('schedule/<int:id>', ScheduleAPIView.as_view(), name='Schedule-API'),

    path('description/<int:id>', DescriptionAPIView.as_view(),
         name='Description-API'),

    path('book-service/<int:id>', BookServiceAPIView.as_view(),
         name='Book-Service-API'),

    path('order-details/<int:id>', OrderDetailsAPIView.as_view(),
         name='Order-details-API'),

    path('tracker/<int:id>', TrackerAPIView.as_view(),
         name='Tracker-API'),

    path('rebook/<int:id>', RebookOrderAPIView.as_view(),
         name='Rebook-API'),

    path('order/<str:uuid>', ChangeOrderStatus.as_view(),
         name='CHANGE-ORDER-STATUS-View'),

    path('change-status/<int:id>', ChangeOrderStatusAPI.as_view(),
         name='rebooking-data'),

    path("recent-booking/", RecentBookingAPIView.as_view(), name='recent-booking')

]
