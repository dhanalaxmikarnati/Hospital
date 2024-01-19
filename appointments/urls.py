from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'), 
    # Ensure the name matches the view function name
    # other URL patterns
]
