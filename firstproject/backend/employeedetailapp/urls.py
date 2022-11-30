from django.urls import path
from .views import Import_csv,displayemployee
urlpatterns=[
     path('addemployee/',Import_csv,name="addemployee"),
      path('displayemployee/<str:key>',displayemployee,name="addemployee"),
]
