from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name="홈페이지"),
]