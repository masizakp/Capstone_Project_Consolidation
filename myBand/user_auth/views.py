from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms


# -------------------------------
# Form for user registration
# -------------------------------
class RegisterForm(forms.ModelForm):
    """
    A custom registration form based on Django's ModelForm.
    Adds a password field using a PasswordInput widget.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# -------------------------------
# View: Handle user registration
# -------------------------------
def register(request):
    """
    Handle user registration.

    If POST: Validate form, hash password, save user, and log in.
    If GET: Render empty registration form.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save until password is hashed
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the new user
            login(request, user)  # Log the user in automatically
            return redirect('user_auth:show_user')  # Redirect to user page
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})


# -------------------------------
# View: Authenticate user on login
# -------------------------------
def authenticate_user(request):
    """
    Authenticate and log in a user.

    If POST: authenticate user credentials; on success, log in and redirect;
    on failure, show error on login page.
    If not POST: redirect to login page.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_auth:show_user')
        else:
            return render(request, 'authentication/login.html', {
                'error': 'Invalid username or password'
            })
    else:
        return redirect('user_auth:login')


# -------------------------------
# View: Show welcome page for logged-in users
# -------------------------------
def show_user(request):
    """
    Display the user's welcome page with their username.
    Assumes the user is already logged in.
    """
    return render(request, 'authentication/user.html', {
        'username': request.user.username
    })


# -------------------------------
# View: Display login form
# -------------------------------
def user_login(request):
    """
    Render the login form page (GET request).
    """
    return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    return redirect('user_auth:login')