from django.urls import path
from inven import views

urlpatterns = [
    path('', views.index, name="index"),
    path('All/', views.All, name="All"),
    path('Computer/', views.Computer, name="Computer"),
    path('Screen/', views.Screen, name="Screen"),
    path('Medical/', views.Medical, name="Medical"),
    path('others1/', views.others1, name="others1"),
    path('others2/', views.others2, name="others2"),
]