from django.db import models

# Create your models here.

#defining the Article model
class Article(models.Model):

    #defining the author of the article as a foreign key to the User model
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    #defining the title of the article as a character field with maximum length of 50 characters
    title = models.CharField(max_length = 50)
    #defining the content of the article as a text field
    content = models.TextField()
    #defining the created date of the article as a date time field that automatically adds the current date and time
    created_date = models.DateTimeField(auto_now_add = True)

    #defining the string representation of the article
    def __str__(self):

        return self.title
