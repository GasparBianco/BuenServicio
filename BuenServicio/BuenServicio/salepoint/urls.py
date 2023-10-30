from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:table>', views.table, name='table'),
    path('<int:table_number>/addproduct', views.order, name='order'),
    path('<int:table_number>/resettable', views.reset_table, name='reset')
    ]