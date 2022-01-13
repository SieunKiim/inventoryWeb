from django.urls import path
from inven import views

urlpatterns = [
    path('', views.index, name="index"),
]