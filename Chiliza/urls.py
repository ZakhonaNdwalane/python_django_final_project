from django.urls import path
from django.contrib.auth import views as auth_views  # Import built-in auth views
from . import views
from django.contrib.auth.decorators import login_required  # Import login_required decorator

urlpatterns = [
    # Public views
    path('', views.home, name='home'),  # Home page, available for everyone
    
    # Restricted views (login required)
    path('services/', login_required(views.services, login_url='login'), name='services'),  # Requires login
    path('risk-calculator/', login_required(views.risk_calculator, login_url='login'), name='risk_calculator'),  # Requires login

    # Registration and authentication URLs
    path('register/', views.register, name='register'),  # Registration view
    path('login/', auth_views.LoginView.as_view(template_name='Chiliza/login.html'), name='login'),  # Login view
     path('logout/', views.custom_logout, name='logout')  # Logout view
]

