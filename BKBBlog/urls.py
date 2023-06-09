"""
URL configuration for BKBBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import necessary modules and packages
from django.contrib import admin
from django.urls import path, include
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL pattern for Django admin site
    path('admin/', admin.site.urls),
    # URL pattern for the root path of the website which maps to the index function in article.views module
    path('', views.index, name = "index"),
    # URL pattern for the about/ path of the website which maps to the about function in article.views module
    path('about/', views.about, name = "about"),
    # Map all URLs starting with "articles/" to the urlpatterns defined in the "article.urls" module
    path('articles/', include("article.urls")),
    # Map all URLs starting with "user/" to the urlpatterns defined in the "user.urls" module
    path('user/', include("user.urls")),
]

# Enable serving media files during development using the specified URL and root directory
if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
