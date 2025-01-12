from django.urls import path
from . import views

urlpatterns = [
    path('', views.buying, name='buying'),
    path('done/', views.done, name='done'),
    path('cancel/', views.cancel, name='cancel'),
    path('logout/', views.logout, name='logout')
]
