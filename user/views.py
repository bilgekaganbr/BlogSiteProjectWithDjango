# Import necessary modules and packages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

# Define the function-based view to handle requests to the user/register/ path of the website
def register(request):

    # Create a new instance of the RegisterForm using the request.POST data, if available
    form = RegisterForm(request.POST or None)

    # Create a context dictionary containing the form object
    context = {
        "form" : form
    }

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

        # Show a success message when the registration is successful
        messages.success(request, "You have successfully registered.")

        # Redirect the user to the index page
        return redirect("index")
    
    else:

         # If the form is not valid, return an HTTP response containing the rendered "register.html" template with the form
        return render(request, "register.html", context)

# Define the function-based view to handle requests to the user/login/ path of the website
def log_in(request):

    # Create a new instance of the LoginForm using the request.POST data, if available
    form = LoginForm(request.POST or None)

    # Create a context dictionary containing the form object
    context = {
        "form" : form
    }

    # Check if the form is valid, i.e., if all required fields have been filled out correctly
    if form.is_valid():
        
        # If the form is valid, extract the username and password from the form data
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # Authenticate the user using the provided username and password
        user = authenticate(username = username, password = password)

        if user is None:
            
            # If authentication fails, display an error message
            messages.info(request, "The user name or password is incorrect.")

            # Return an HTTP response containing the rendered "login.html" template with the form
            return render(request, "login.html", context)
        
        else:
            
            # If authentication succeeds, display a success message
            messages.success(request, "You have successfully login.")

            # Log in the user
            login(request, user)

            # Redirect to the index page
            return redirect("index")
    else:

        # If the form is not valid, return an HTTP response containing the rendered "login.html" template with the form
        return render(request, "login.html", context)

# Define the function-based view to handle requests to the user/logout/ path of the website
def log_out(request):

    # Log out the user
    logout(request)

    # Display a success message
    messages.success(request, "You have successfully logout.")

    # Redirect to the index page
    return redirect("index")
