from django.urls import path 
from accounts.views import Home,LoginView

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login',LoginView.as_view(),name='login')
]
