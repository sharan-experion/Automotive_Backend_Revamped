from django.urls import path,include
from rest_framework import routers
from .views import getcategory,addproducts,displayproducts,sortproduct,updateproduct,printproductdetails,productexcel

router=routers.DefaultRouter(trailing_slash=False)
router.register(r'printproductdetails/',printproductdetails,basename='printproduct')
urlpatterns=[
    path('category',getcategory,name="category1"),
    path('addproduct/',addproducts,name="category"),
    path('displayproduct/',displayproducts,name="category"),
    path('sortproduct/',sortproduct,name="category"),
    path('updateproduct/<str:pk>',updateproduct,name="category"),
    
    path('excelproductupload/',productexcel,name="category"),
    path(r'',include(router.urls))
        
]