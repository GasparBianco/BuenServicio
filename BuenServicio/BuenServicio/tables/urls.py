from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_mesas, name='tables'),
    path('deleteonetable/', views.deleteOneTable, name='delete_one_table'),
    path('deletealltables/', views.deleteAllTables, name='delete_all_tables'),
    path('addonetable/', views.addOneTable, name='add_one_table'),
    path('addmanytables/', views.addManyTables, name='add_many_tables'),
    ]