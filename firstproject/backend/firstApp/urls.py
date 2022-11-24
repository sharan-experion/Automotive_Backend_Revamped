from.views import register,login
from django.urls import path

urlpatterns=[
    path('signup/',register,name="register"),
    path('login/',login,name="routes")
    
    
]
