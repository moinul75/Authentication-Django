from django import forms 
from .models import * 


#custom login forms 
class LoginForm(forms.Form):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs.update({'class':'form-control'})
    username = forms.CharField(
        max_length=150,
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class':'form-control'})
            
        
    class Meta: 
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password2'
        )
        
    def clean_password(self, *args, **kwargs):
        #get this two pass 
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        #if not matched raise a validation errors 
        if password != password2:
            raise forms.ValidationError('Password Does not matched')
        return password2
    
    def save(self,commit=True,*args, **kwargs):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    
        
   
        
       
    