from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.data, name='home'),
    path('', views.index, name='index'),
]