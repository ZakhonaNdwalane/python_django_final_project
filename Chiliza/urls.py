from django.urls import path
from django.contrib.auth import views as auth_views  # Import built-in auth views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('risk-calculator/', views.risk_calculator, name='risk_calculator'),  # Use the view, login will be enforced by @login_required

    # Registration and authentication URLs
    path('register/', views.register, name='register'),  # Registration view
    path('login/', auth_views.LoginView.as_view(template_name='Chiliza/login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout view
]
