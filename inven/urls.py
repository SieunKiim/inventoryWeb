from django.urls import path
from inven import views

urlpatterns = [
    path('', views.index, name="index"),
    path('All/', views.all, name="All"),
    path('user/add/', views.add_user, name="add_user"),  # 이게 맞아?
    path('Computer/', views.computer, name="Computer"),
    path('Screen/', views.screen, name="Screen"),
    path('Medical/', views.medical, name="Medical"),
    path('others1/', views.others1, name="others1"),
    path('others2/', views.others2, name="others2"),
]
