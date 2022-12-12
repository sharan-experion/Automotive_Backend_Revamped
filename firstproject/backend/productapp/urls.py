from django.urls import path
from .views import getcategory,addproducts,displayproducts,sortproduct,updateproduct,printproductdetails,productexcel
urlpatterns=[
    path('category',getcategory,name="category1"),
    path('addproduct/',addproducts,name="category"),
    path('displayproduct/',displayproducts,name="category"),
    path('sortproduct/',sortproduct,name="category"),
    path('updateproduct/<str:pk>',updateproduct,name="category"),
    path('printproductdetails/',printproductdetails,name="category"),
    path('excelproductupload/',productexcel,name="category"),



        
]