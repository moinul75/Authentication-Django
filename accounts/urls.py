from django.urls import path 
from accounts.views import Home

urlpatterns = [
    path('',Home.as_view(),name='home'),
]
