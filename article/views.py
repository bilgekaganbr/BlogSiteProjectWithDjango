#importing necessary modules and packages
from django.shortcuts import render, HttpResponse

# Create your views here.

#define the function-based view to handle requests to the root path of the website
def index(request):

     #return an HTTP response containing the rendered "index.html" template
     return render(request, "index.html")
