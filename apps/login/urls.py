from django.urls import path
from .views import login_view, register_view, home_view, password_reset_request_view, password_reset_confirm_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),
    path('password_reset/', password_reset_request_view, name='password_reset'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('logout/', logout_view, name='logout'),
]
