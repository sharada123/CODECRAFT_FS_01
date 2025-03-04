from django.urls import path
from . import views
urlpatterns = [
    path('home',views.homepage,name='home'),
    path('',views.register_page,name='RegisterPage'),
    path('login_page',views.login_page,name='LoginPage'),
    path('login',views.login_user,name='Login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_user,name='Logout'),
    path('admin-dashboard',views.admin_page,name='admin_dashboard'),
    path('user-dashboard',views.user_page,name='user_dashboard'),
]