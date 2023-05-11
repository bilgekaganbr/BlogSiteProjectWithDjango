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
    
    class Meta:

        # Define the ordering of the model instances in order to sort articles in reverse order by created date
        ordering = ['-created_date']
    
class Comment(models.Model):

    # Define the article of the comment as a foreign key to the Article model
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Article", related_name = "comments")
    # Define the author of the comment as a character field with maximum length of 50 characters
    comment_author = models.CharField(max_length = 50, verbose_name = "Name")
    # Define the content of the comment as a character field with maximum length of 200 characters
    comment_content = models.CharField(max_length = 200, verbose_name = "Comment")
    # Define the created date of the comment as a date time field that automatically adds the current date and time
    comment_date = models.DateTimeField(auto_now_add = True)

    # Define the string representation of the comment
    def __str__(self):

        return self.comment_content
    
    class Meta:

        # Define the ordering of the model instances in order to sort comments in reverse order by comment date
        ordering = ['-comment_date']