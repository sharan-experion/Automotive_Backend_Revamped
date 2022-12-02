from django.urls import path
from .views import getservices,getcustomer,addcustomer
urlpatterns=[
     path('getservices/',getservices,name="services"),
     path('getcustomer/<str:key>',getcustomer,name="get customer"),
     path('addcustomer/',addcustomer,name="add customer"),
]