"""
    URL configuration for the polls app.

    Maps URL paths to their corresponding view functions.

    Includes:
    - List of latest questions
    - Question details
    - Results display
    - Voting endpoint
    - Blog detail pattern with regex
    - User authentication URLs
"""

from django.urls import path, re_path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    re_path(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.detail),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
]
