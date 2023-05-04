# Import necessary modules and packages
from django.contrib import admin
from django.urls import path
from . import views

# Set a name to the app
app_name = "article"

urlpatterns = [
    # URL pattern for the articles/create/ path of the website which maps to the index function(for now) in article.views module
    path('create/', views.index, name = "index"),
]