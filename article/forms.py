from django import forms
from .models import Article

# Define a article form from article model that users can fill out to create an article
class ArticleForm(forms.ModelForm):

    class Meta:
        
        # Set the Meta options for the form, including the model and the fields to include
        model = Article
        fields = ["title", "content"]