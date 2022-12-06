from django.urls import path
from .views import getrevenuereport

urlpatterns=[
    path('getrevenue/<str:key>',getrevenuereport,name="services"),
]