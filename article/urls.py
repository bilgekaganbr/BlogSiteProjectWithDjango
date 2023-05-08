# Import necessary modules and packages
from django.contrib import admin
from django.urls import path
from . import views

# Set a name to the app
app_name = "article"

urlpatterns = [
    # URL pattern for the articles/dashboard/ path of the website which maps to the dashboard function in article.views module
    path('dashboard/', views.dashboard, name = "dashboard"),
    # URL pattern for the articles/addarticle/ path of the website which maps to the addArticle function in article.views module
    path('addarticle/', views.addArticle, name = "addarticle")
]