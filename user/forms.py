from django import forms

# Define a registration form that users can fill out to create an account
class RegisterForm(forms.Form):

    # Define the form inputs for the username and password
    username = forms.CharField(max_length = 50, label = "Username")
    password = forms.CharField(max_length = 20, label = "Password", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length = 20, label = "Confirm Password", widget = forms.PasswordInput)

    # Perform validation on the form data and return a cleaned data dictionary
    def clean(self):

        # Get the cleaned data for the username, password, and confirm fields
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            
            # Check if the password and confirm fields match, and raise a validation error if they don't
            raise forms.ValidationError("Passwords do not match.")
        
        # If the form data is valid, return a cleaned data dictionary containing the username and password
        values = {  
            "username" : username,
            "password" : password,
        }

        return values