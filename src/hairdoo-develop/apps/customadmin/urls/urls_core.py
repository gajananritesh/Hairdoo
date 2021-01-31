from django.urls import path, include
from django.views.generic import TemplateView
from . import views
app_name = 'core'
urlpatterns = [
    #path("", TemplateView.as_view(template_name="core/index.html"), name="index"),
    path("", views.UserListView.as_view(), name="homepage"),
    path("users-all/", views.AllUserListView.as_view(), name="all-users"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/password/", views.UserPasswordView.as_view(), name="user-password"),
    path("registered-users/", views.RegisteredUserListView.as_view(), name="registred-users"),
    path("registered-users/delete", views.ProjectDeleteView, name="user-delete"),

    #password_check URL

    path("password_check/", views.is_corrrect_password, name="password_check"),

    path("registred-users/<int:pk>/update/", views.RegistredUserUpdateView.as_view(), name="registred-user-update"),

    path("user-detail/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),

    path("bookings/", views.UserBookingListView.as_view(), name="bookings"),

    path("booked-user-detail/<int:id>/", views.BookedServiceUserDetailView.as_view(), name="booked-user-detail"),

    #path("edit-booking/<int:id>/", views.EditServiceView.as_view(), name="edit-book-view"),

    path("edit-booking-form/<int:id>/",views.edit_booking,name = "edit-booking"),

    path("booking/delete", views.OrderDeleteView, name="booking-delete"),



]