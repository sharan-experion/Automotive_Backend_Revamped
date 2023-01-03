from django.urls import path
from .views import getservices,getcustomer,addcustomer,addestimate,getservicehistory,getestimateproduct,getestimateservices,getproduct_for_estimation,update_estimate_product,update_Work_status
urlpatterns=[
     path('getservices/',getservices,name="services"),
     path('getcustomer/<str:key>/<str:user>',getcustomer,name="get customer"),
     path('addcustomer/',addcustomer,name="add customer"),
     path('addestimate/',addestimate,name="add estimate"),
     path('estimatedetails/<str:key>/<str:user>',getservicehistory,name="get estimate"),
     path('estimateproducts/<str:key>',getestimateproduct,name="get estimate product"),
     path('estimateservices/<str:key>',getestimateservices,name="get estimate product"),
     path('getestimateproducts/',getproduct_for_estimation,name="services"),
     path('updateestimateproducts/',update_estimate_product,name="update_estimate"),
     path('updateworkstatus/<str:key>',update_Work_status,name="update_estimate"),
]
