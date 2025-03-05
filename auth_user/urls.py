from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('login',views.login_user,name='Login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_user,name='Logout'),
    path('admin-dashboard',views.admin_page,name='admin_dashboard'),
    path('user-dashboard',views.user_page,name='user_dashboard'),
    path('verify-otp',views.verify_otp,name='VerifyOtp'),
]