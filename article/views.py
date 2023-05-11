# Import necessary modules and packages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article, Comment

# Create your views here.

# Define the function-based view to handle requests to the root path of the website
def index(request):

     # Return an HTTP response containing the rendered "index.html" template
     return render(request, "index.html")

# Define the function-based view to handle requests to the "/about" path of the website
def about(request):

     # Return an HTTP response containing the rendered "about.html" template
     return render(request, "about.html")

def articles(request):

     # Retrieve the keyword parameter from the request's GET parameters
     keyword = request.GET.get("keyword")

     # Check if a keyword is provided
     if keyword:

          # Retrieve all articles from the database based on the provided keyword
          articles = Article.objects.filter(title__contains = keyword)

          # Return an HTTP response containing the rendered "articles.html" template with the filtered articles
          return render(request, "articles.html", {"articles" : articles})

     # If no keyword is provided, retrieve all articles from the database
     articles = Article.objects.all()

     # Return an HTTP response containing the rendered "articles.html" template with all articles
     return render(request, "articles.html", {"articles" : articles})

# Apply login_required decorator to restrict access to authenticated users only and redirect the unauthenticated users to the login page
@login_required(login_url = "user:login")
# Define the function-based view to handle requests to the "/articles/dashboard" path of the website
def dashboard(request):
     
     # Retrieve all articles from the database authored by the current user
     articles = Article.objects.filter(author = request.user)

     # Create a context dictionary containing the form object
     context = {
          "articles" : articles
     }

     # Return an HTTP response containing the rendered "dashboard.html" template with articles
     return render(request, "dashboard.html", context)

# Apply login_required decorator to restrict access to authenticated users only and redirect the unauthenticated users to the login page
@login_required(login_url = "user:login")
# Define the function-based view to handle requests to the "/articles/addarticle" path of the website
def addArticle(request):

     # Create a new instance of the ArticleForm using the request.POST data and request.FILE, if available
     form = ArticleForm(request.POST or None, request.FILES or None)

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

          # Redirect to the article dashboard page
          return redirect("article:dashboard")

     # Return an HTTP response containing the rendered "addarticle.html" template with the form
     return render(request, "addarticle.html", context)

# Define the function-based view to handle requests to the /articles/article/articleid path of the website
def detail(request, id):
     
     # Retrieve the article object with the given id from the database or return a 404 page if not found
     article = get_object_or_404(Article, id = id)

     # Retrieve all comments associated with the article
     comments = article.comments.all()

     # Return an HTTP response containing the rendered "detail.html" template with the article 
     return render(request, "detail.html", {"article" : article, "comments" : comments})

# Apply login_required decorator to restrict access to authenticated users only and redirect the unauthenticated users to the login page
@login_required(login_url = "user:login")
# Define the function-based view to handle requests to the /articles/update/articleid path of the website
def update(request, id):

     # Retrieve the article object with the given id from the database or return a 404 page if not found
     article = get_object_or_404(Article, id = id)

     # Create a new instance of the ArticleForm using the request.POST data and request.FILE, if available and send the article to the form
     form = ArticleForm(request.POST or None, request.FILES or None, instance = article)

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
          messages.success(request, "Article successfully updated.")

          # Redirect to the article dashboard page
          return redirect("article:dashboard")

     # Return an HTTP response containing the rendered "update.html" template with the form
     return render(request, "update.html", context)

# Apply login_required decorator to restrict access to authenticated users only and redirect the unauthenticated users to the login page
@login_required(login_url = "user:login")
# Define the function-based view to handle requests to the /articles/delete/articleid path of the website
def delete(request, id):

     # Retrieve the article object with the given id from the database or return a 404 page if not found
     article = get_object_or_404(Article, id = id)

     # Delete the article object
     article.delete()

     # If deleting article is successful, display a success message
     messages.success(request, "Article successfully deleted.")

     # Redirect to the article dashboard page
     return redirect("article:dashboard")

# Apply login_required decorator to restrict access to authenticated users only and redirect the unauthenticated users to the login page
@login_required(login_url = "user:login")
# Define the function-based view to handle requests to the /articles/comment/articleid path of the website to make comment
def comment(request, id):

     # Retrieve the article object with the given id from the database or return a 404 page if not found
     article = get_object_or_404(Article, id = id)

     if request.method == "POST":

          # Retrieve the comment author and content from the POST data
          comment_author = request.POST.get("comment_author")
          comment_content = request.POST.get("comment_content")

          # Create a new Comment object
          newComment = Comment(comment_author = comment_author, comment_content = comment_content)
          # Associate the comment with the article
          newComment.article = article
          
          # Save the new comment obeject to the database
          newComment.save()

     # Redirect to the article detail page with the given id
     return redirect(reverse("article:detail", kwargs = {"id" : id}))