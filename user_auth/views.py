from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
        fields = ['username', 'email', 'password']from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms

# -------------------------------
# Form for user registration
# -------------------------------
class RegisterForm(forms.ModelForm):
    """
    A custom registration form based on Django's ModelForm.

    :param password: Password field with hidden input
    :type password: str
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

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Redirects to user page after successful registration or renders registration form
    :rtype: HttpResponse
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

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Redirects to user page on success, or login page with error on failure
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('user_auth:show_user')
        else:
            # Show error if authentication fails
            return render(request, 'authentication/login.html', {
                'error': 'Invalid username or password'
            })
    else:
        return redirect('user_auth:login')  # Redirect to login if not POST


# -------------------------------
# View: Show welcome page for logged-in users
# -------------------------------
def show_user(request):
    """
    Display the user's welcome page with their username.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered user welcome page with username in context
    :rtype: HttpResponse
    """
    return render(request, 'authentication/user.html', {
        'username': request.user.username
    })


# -------------------------------
# View: Display login form
# -------------------------------
def user_login(request):
    """
    Render the login form page.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered login page template
    :rtype: HttpResponse
    """
    return render(request, 'authentication/login.html')



# -------------------------------
# View: Handle user registration
# -------------------------------
def register(request):
    """
    Handle user registration.

    - If the request is POST, validate the form and create a new user.
    - Set the password securely using `set_password`.
    - Optionally log in the user immediately after registration.
    - If the request is GET, render an empty registration form.
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

    - If the request is POST, extract credentials and use Django's `authenticate`.
    - If successful, log the user in and redirect to the user page.
    - If authentication fails, show an error on the login page.
    - If not POST, redirect to the login page.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('user_auth:show_user')
        else:
            # Show error if authentication fails
            return render(request, 'authentication/login.html', {
                'error': 'Invalid username or password'
            })
    else:
        return redirect('user_auth:login')  # Redirect to login if not POST


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
    Render the login form page.

    This view is accessed via GET to show the login screen.
    """
    return render(request, 'authentication/login.html')
