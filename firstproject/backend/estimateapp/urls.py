from django.urls import path
from .views import getservices,getcustomer
urlpatterns=[
     path('getservices/',getservices,name="services"),
      path('getcustomer/<str:key>',getcustomer,name="services"),
]