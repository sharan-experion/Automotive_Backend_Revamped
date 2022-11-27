from django.urls import path
from .views import getcategory,addproducts,displayproducts,sortproduct,updateproduct
urlpatterns=[
    path('category',getcategory,name="category"),
    path('addproduct/',addproducts,name="category"),
    path('displayproduct/<str:key>',displayproducts,name="category"),
    path('sortproduct/',sortproduct,name="category"),
    path('updateproduct/<str:pk>',updateproduct,name="category"),



        
]