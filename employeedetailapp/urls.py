from django.urls import path
from .views import Import_csv,displayemployee,singleEmployee
urlpatterns=[
     path('addemployee/',Import_csv,name="addemployee"),
      path('displayemployee/<str:key>',displayemployee,name="addemployee"),
      path('singleemployee/',singleEmployee,name="addemployee"),
]
