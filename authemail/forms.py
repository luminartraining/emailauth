from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['email']
class LoginForm(forms.Form):
    email=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)
    def clean(self):
        print("inside clean validate user and password")