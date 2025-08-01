# accounts/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    # Note: 'home' is now handled by the 'books' app
    path('profile/', views.profile_settings, name='profile_settings'), # New profile settings URL

    # Django's built-in password change views
    # These views handle the logic, we just provide the templates
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html', success_url='/accounts/password_change/done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]