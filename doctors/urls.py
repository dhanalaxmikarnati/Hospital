from django.urls import path
from . import views

urlpatterns = [
    path('',views.doctors) ,
    path('hospital',views.hospital)
]
