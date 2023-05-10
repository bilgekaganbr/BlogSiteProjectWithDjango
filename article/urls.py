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
    path('addarticle/', views.addArticle, name = "addarticle"),
    # URL pattern for the articles/article/article id/ path of the website which maps to the detail function in article.views to show article detail
    path('article/<int:id>/', views.detail, name = "detail"),
    # URL pattern for the articles/update/article id/ path of the website which maps to the update function in article.views to update article
    path('update/<int:id>/', views.update, name = "update"),
    # URL pattern for the articles/delete/article id/ path of the website which maps to the delete function in article.views to delete article
    path('delete/<int:id>/', views.delete, name = "delete"),
    # URL pattern for the articles' root path of the website which maps to the articles function in article.views module to show articles
    path('', views.articles, name = "articles"),
    # URL pattern for the articles/comment/article id/ path of the website which maps to the comment function in article.views to add a comment
    path('comment/<int:id>/', views.comment, name = "comment"),
]