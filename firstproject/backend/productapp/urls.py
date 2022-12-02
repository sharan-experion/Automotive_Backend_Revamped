from django.urls import path
from .views import getcategory,addproducts,displayproducts,sortproduct,updateproduct,printproductdetails
urlpatterns=[
    path('category',getcategory,name="category"),
    path('addproduct/',addproducts,name="category"),
    path('displayproduct/',displayproducts,name="category"),
    path('sortproduct/',sortproduct,name="category"),
    path('updateproduct/<str:pk>',updateproduct,name="category"),
    path('printproductdetails/<str:key>',printproductdetails,name="category"),



        
]