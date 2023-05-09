# Import necessary modules and packages
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Define the Article model
class Article(models.Model):

    # Define the author of the article as a foreign key to the User model
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    # Define the title of the article as a character field with maximum length of 50 characters
    title = models.CharField(max_length = 50)
    # Define the content of the article as a text field
    content = RichTextField()
    # Define the created date of the article as a date time field that automatically adds the current date and time
    created_date = models.DateTimeField(auto_now_add = True)
    # Define the article image field as a file field, allowing it to be blank and nullable
    article_image = models.FileField(blank = True, null = True, verbose_name = "Add image to the article")

    # Define the string representation of the article
    def __str__(self):

        return self.title
