from.import views
from django.urls import path

urlpatterns=[
    path('signup/',views.postuserdetails,name="routes"),
    path('login/',views.logindetails,name="routes")
    
    
]
