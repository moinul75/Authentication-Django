from django.urls import path 
from accounts.views import Home,LoginView,Logout,RegisterView

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('register',RegisterView.as_view(),name='register')
]
