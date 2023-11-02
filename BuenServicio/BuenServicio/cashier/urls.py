from django.urls import path
from . import views

urlpatterns = [
    path('', views.cashier, name='cashier'),
    path('pay/', views.pay, name='pay'),
    path('open_cashier/', views.open_cashier, name='open_cashier'),
    path('close/cashier', views.close_cashier, name='close_cashier'),
    ]

