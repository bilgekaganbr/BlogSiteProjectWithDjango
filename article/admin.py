from django.contrib import admin

# Import the Article model from the models.py file
from.models import Article, Comment

# Register your models here.

# Register the Article model in the admin site
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    # Specify the fields to be displayed in the admin list view
    list_display = ["title", "author", "created_date"]

    # Specify the fields to be linked to the article detail view in the admin list view
    list_display_links = ["title", "created_date"]

    # Specify the fields to be searchable in the admin list view
    search_fields = ["title"]

    # Specify the fields to be used as filters in the admin list view
    list_filter = ["created_date"]

    # Define the meta class for the ArticleAdmin model
    class Meta:

        # Specify the model for the ArticleAdmin model
        model = Article 

# Register the Comment model in the admin site
admin.site.register(Comment)

