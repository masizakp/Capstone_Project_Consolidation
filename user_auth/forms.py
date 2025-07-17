from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    """
    A custom user registration form that extends Django's UserCreationForm.

    Adds a required 'first_name' field and applies Bootstrap styling to all fields.
    """

    # Additional field not included in UserCreationForm by default
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Bootstrap styling
    )

    class Meta:
        model = User  # Use Django's built-in User model
        fields = ['username', 'first_name', 'password1', 'password2']

        # Apply Bootstrap CSS classes to input fields
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
