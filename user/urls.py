# Import necessary modules and packages
from django.contrib import admin
from django.urls import path
from . import views

# Set a name to the app
app_name = "user" 

urlpatterns = [
    # URL pattern for the user/register/ path of the website which maps to register function in user.views module
    path('register/', views.register, name = "register"),
    # URL pattern for the user/login/ path of the website which maps to login function in user.views module
    path('login/', views.log_in, name = "login"), 
    # URL pattern for the user/logout/ path of the website which maps to logout function in user.views module
    path('logout/', views.log_out, name = "logout"),
]