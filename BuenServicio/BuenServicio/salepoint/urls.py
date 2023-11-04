from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:table>', views.table, name='table'),
    path('count/<int:table_number>', views.count, name='count'),
    path('payment/<int:table>', views.payment, name='payment'),
    path('print/<int:table_number>', views.reprint, name='reprint'),
    path('<int:table_number>/addproduct', views.order, name='order'),
    path('<int:table_number>/resettable', views.reset_table, name='reset')
    ]