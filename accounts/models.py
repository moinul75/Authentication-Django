from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from accounts.manager import UserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        validators=[UnicodeUsernameValidator, ],
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        default=None
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    
    
    class Meta: 
        ordering = ['-date_joined']
        
    def __str__(self):
        return self.username
    
    
