from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self,email,username,password,**extra_fields):
        if not username:
            raise ValueError('user must have an username')
        if not email:
            raise ValueError('user must have an email')
        
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email  = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,username,password,**extra_fields):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    