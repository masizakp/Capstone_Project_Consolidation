"""
    URL configuration for the user_auth app.

    Defines URL routes for user authentication, including:
    - Login page
    - User authentication POST handler
    - User dashboard
    - User registration
"""

from django.urls import path
from user_auth import views

# App namespace for template URL resolution (e.g., {% url 'user_auth:login' %})
app_name = 'user_auth'

# URL patterns for the authentication system
urlpatterns = [
    # Login page: shows the login form
    path('', views.user_login, name='login'),
    
    # Form POST handler for logging in users
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    
    # User dashboard page shown after login/registration
    path('user/', views.show_user, name='show_user'),
    
    # Registration page to create a new user account
    path('register/', views.register, name='register'),
]
