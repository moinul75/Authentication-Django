from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login'
    template_name = 'accounts/home.html'


#login 
class LoginView(generic.View):
    def get(self,*args, **kwargs):
        return render(self.request, 'accounts/login.html')
        
    
    def post(self,*args, **kwargs):
        pass 
    