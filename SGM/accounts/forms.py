from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()


class SignupForm(forms.Form):
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), required=True)
    first_name= forms.CharField(max_length=100, help_text='Required')
    last_name= forms.CharField(max_length=100, help_text='Required')
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','password')
    
    
    def save(self):
            data = self.cleaned_data
            user = User(
                email=data['email'],
                is_active=False,
                password=make_password(data['password'])
            )
            return user.save()