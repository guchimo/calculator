from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('new', calculate, name='calculate_view'),
    path('signup', user_registration, name='signup_view'),
    path('login', user_login, name='login_view'),
    path('logout', LogoutView.as_view(template_name='core/user_logout.html'), name='logout_view'),
    path('profile/<int:pk>', UserUpdateView.as_view(), name='profile_view'),
    path('history', HistoryListView.as_view(), name='history_view'),
]
