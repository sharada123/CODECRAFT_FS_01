from django import forms
from .models import CustomUser
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password','confirm_password','role']
        widgets={'username':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'username'}),
                'email':forms.EmailInput(attrs={'class':'form-control mt-2 ','placeholder':'email'}),
                'password':forms.PasswordInput(attrs={'class':'form-control mt-2 ','placeholder':'password'}),
                'confirm_password':forms.PasswordInput(attrs={'class':'form-control mt-2 ','placeholder':'confirm password'}),
                'role':forms.Select(choices=CustomUser.role_choices,attrs={'class':'form-control mt-2 ','placeholder':'role'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Password'})
    )