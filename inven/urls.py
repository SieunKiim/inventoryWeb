from django.urls import path
from inven import views

urlpatterns = [
    path('', views.index, name="index"),
    path('All/', views.all, name="All"),
    path('user/', views.add_user, name="add_user"),  # 이게 맞아?
    path('Computer/', views.computer, name="Computer"),
    path('Screen/', views.screen, name="Screen"),
    path('Medical/', views.medical, name="Medical"),
    path('Others/', views.others, name="Others"),

    # 기기 추가
    path('Computer/add/', views.addComputer, name="addComputer"),
    path('Screen/add/', views.addScreen, name="addScreen"),
    path('Medical/add/', views.addMedical, name="addMedical"),
    path('Others/add/', views.addOthers, name="addOthers"),


    # 이건 안쓸듯?
    path('inven_user/', views.inven_user, name="inven_user"),
]

