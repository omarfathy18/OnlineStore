from django.urls import path
from . import views

urlpatterns = [
    path('', views.item, name='item'),
    path('logout/', views.logout, name='logout'),
]
