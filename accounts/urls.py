# urls.py
from django.urls import path
from .views import SignupView, LoginView, ProtectedView, HotelList, HotelDetail
from .views import BookingCreateView, PropertyCreateView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('userlogin/', LoginView.as_view(), name='userlogin'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('hotels/', HotelList.as_view(), name='hotels'),
    path('hotels/<str:hotel_id>/', HotelDetail.as_view(), name='hotel-detail'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking-create'),
    path('properties/create/', PropertyCreateView.as_view(), name='property-create'),
]
