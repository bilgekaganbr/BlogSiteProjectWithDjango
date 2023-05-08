# Import necessary modules and packages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .forms import ArticleForm
from .models import Article

# Create your views here.

# Define the function-based view to handle requests to the root path of the website
def index(request):

     # Return an HTTP response containing the rendered "index.html" template
     return render(request, "index.html")

# Define the function-based view to handle requests to the "/about" path of the website
def about(request):

     # Return an HTTP response containing the rendered "about.html" template
     return render(request, "about.html")

# Define the function-based view to handle requests to the "/articles/dashboard" path of the website
def dashboard(request):

     articles = Article.objects.filter(author = request.user)

     context = {
          "articles" : articles
     }

     # Return an HTTP response containing the rendered "dashboard.html" template 
     return render(request, "dashboard.html", context)

# Define the function-based view to handle requests to the "/articles/addarticle" path of the website
def addArticle(request):

     # Create a new instance of the ArticleForm using the request.POST data, if available
     form = ArticleForm(request.POST or None)

     # Create a context dictionary containing the form object
     context = {
          "form" : form
     }

     if form.is_valid():
          
          # If the form is valid, save the article object without committing to the database yet
          article = form.save(commit = False)

          # Set the author of the article as the currently authenticated user
          article.author = request.user

          # Save the article to the database
          article.save()

          # If adding article is successful, display a success message
          messages.success(request, "Article successfully created.")

          # Redirect to the index page
          return redirect("index")

     # Return an HTTP response containing the rendered "addarticle.html" template
     return render(request, "addarticle.html", context)