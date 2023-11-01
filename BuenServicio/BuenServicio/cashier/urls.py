from django.urls import path
from . import views

urlpatterns = [
    path('<str:message>', views.cashier, name='cashier'),
    path('', views.cashier, name='cashier'),
    path('open_cashier/', views.open_cashier, name='open_cashier'),
    path('close/cashier', views.close_cashier, name='close_cashier'),
    ]

