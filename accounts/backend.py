from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailbackendAuthentication(ModelBackend):
    def authenticate(self, request, username= None , password=None,**kwargs):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            else:
                return None
        except ObjectDoesNotExist:
            pass 
    def get_user(self,user_id):
        try:
            user = User.objects.get(id =user_id)
            if user: 
                return user
            else: 
                return None
        except ObjectDoesNotExist:
            pass 
            