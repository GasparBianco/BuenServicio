from django.urls import path
from . import views

urlpatterns = [
    path('', views.cashier_home, name='cashier_home'),
    path('reset/', views.reset_history, name='reset_history'),
    path('cashier/', views.cashier, name='cashier'),
    path('history/', views.history, name='sold_history'),
    path('pay/', views.pay, name='pay'),
    path('open_cashier/', views.open_cashier, name='open_cashier'),
    path('close/cashier', views.close_cashier, name='close_cashier'),
    ]

