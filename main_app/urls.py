from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.data, name='home'),
    path('', views.index, name='index'),
]