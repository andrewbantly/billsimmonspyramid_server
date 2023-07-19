from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.data, name='home'),
    path('api/original', views.original, name='home'),
    path('', views.index, name='index'),
]