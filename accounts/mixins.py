from django.shortcuts import render,redirect

class LogOutRequiredMixins(object):
    def dispatch(self,*args, **kwargs):
        if self.request.user.is_authenticated: 
            return redirect('home')
        return super(LogOutRequiredMixins,self).dispatch(*args, **kwargs)