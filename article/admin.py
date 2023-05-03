from django.contrib import admin

# Importing the Article model from the models.py file
from.models import Article

# Register your models here.

# Registering the Article model in the admin site
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    # Specifying the fields to be displayed in the admin list view
    list_display = ["title", "author", "created_date"]

    # Specifying the fields to be linked to the article detail view in the admin list view
    list_display_links = ["title", "created_date"]

    # Specifying the fields to be searchable in the admin list view
    search_fields = ["title"]

    # Specifying the fields to be used as filters in the admin list view
    list_filter = ["created_date"]

    # Defining the meta class for the ArticleAdmin model
    class Meta:

        # Specifying the model for the ArticleAdmin model
        model = Article 

