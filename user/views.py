# Import necessary modules and packages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

# Define the function-based view to handle requests to the user/register/ path of the website
def register(request):

    # Create a new instance of the RegisterForm using the request.POST data, if available
    form = RegisterForm(request.POST or None)

    # Check if the form is valid, i.e., if all required fields have been filled out correctly
    if form.is_valid():
        # If the form is valid, extract the username and password from the form data
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # Create a new User object with the extracted username
        newUser = User(username = username)
        # Set the password for the new User object using the extracted password(it will be hashed)
        newUser.set_password(password)

        # Save the new User object to the database
        newUser.save()

        # Log in the newly registered user
        login(request, newUser)

        # Redirect the user to the index page
        return redirect("index")
    
    else:

        # If the form is not valid, create a context dictionary containing the form object
        context = {
            "form" : form
        }

         # Render the register.html template with the context dictionary
        return render(request, "register.html", context)

def log_in(request):

    return render(request, "login.html")

def log_out(request):

    pass
