from django.shortcuts import render,redirect
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages 
from .mixins import LogOutRequiredMixins
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login'
    template_name = 'accounts/home.html'


#login 
@method_decorator(never_cache,name='dispatch')
class LoginView(LogOutRequiredMixins,generic.View):
    def get(self,*args, **kwargs):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(self.request, 'accounts/login.html',context)
        
    
    def post(self,*args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(
                self.request,
                username=username,
                password =password
            )

            if user: 
                login(self.request, user)
                return redirect('home')
            else:
                messages.warning(self.request, f"Wrong Cradentials")
                return redirect('login')
        context = {
            'form': form
        }
        return render(self.request, 'accounts/login.html',context)
        
    
#logout 
class Logout(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')
    