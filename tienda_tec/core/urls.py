from django.urls import path
from . import views

core_urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
