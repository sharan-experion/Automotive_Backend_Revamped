from django.urls import path
from .views import Import_csv
urlpatterns=[
     path('addemployee/',Import_csv,name="addemployee"),
]