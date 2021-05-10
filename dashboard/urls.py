from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'dashboard-home'),
    path('laundry-request/', views.LaundryCreateView.as_view(), name = 'dashboard-laundry'),
    path('mess-menu/', views.menu, name = 'dashboard-menu'),
    path('night-canteen/', views.canteen, name = 'dashboard-canteen'),
    path('room-cleaning/', views.clean, name = 'dashboard-clean')
]
