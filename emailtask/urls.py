    # personal_details/urls.py

from django.urls import path
from . import views

app_name = 'emailtask'

urlpatterns = [
    path('request/', views.request_details, name='request-details'),
    path('request/<str:username>/', views.request_details, name='request_details'),
]
