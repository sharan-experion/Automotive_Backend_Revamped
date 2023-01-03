from.views import register,login,userview,logout
from django.urls import path

urlpatterns=[
    path('signup/',register,name="register"),
    path('login/',login,name="routes"),
    path('user/',userview,name="routes"),
    path('logout/',logout,name="routes")

    
    
]
