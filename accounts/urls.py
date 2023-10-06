from django.urls import path 
from accounts.views import Home,LoginView,Logout

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout')
]
