# Import necessary modules and packages
from django.shortcuts import render, HttpResponse

# Create your views here.

# Define the function-based view to handle requests to the root path of the website
def index(request):

     # Return an HTTP response containing the rendered "index.html" template
     return render(request, "index.html")

# Define the function-based view to handle requests to the "/about" path of the website
def about(request):

     # Return an HTTP response containing the rendered "about.html" template
     return render(request, "about.html")
