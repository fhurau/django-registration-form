from django import forms
from .validators import validate_password_strength

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[validate_password_strength]
    )
