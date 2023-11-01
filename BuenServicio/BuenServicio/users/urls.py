from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('add/', views.add_user, name='addusers'),
    path('delete/<str:username>', views.delete_user, name='delete_user')
    ]

